import pygame
import random
import sys
import logging
from config import *
from pieces import PIECES, get_piece_count, get_piece_name, get_piece_color, get_piece_border_color
from ui_components import GameUI

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize pygame with error handling
try:
    pygame.init()
    logger.info("Pygame initialized successfully")
except pygame.error as e:
    logger.error(f"Failed to initialize pygame: {e}")
    sys.exit(1)

try:
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()
    logger.info("Display initialized successfully")
except pygame.error as e:
    logger.error(f"Failed to initialize display: {e}")
    pygame.quit()
    sys.exit(1)

class TetrisError(Exception):
    """Base exception for Tetris game errors"""
    pass

class InvalidMoveError(TetrisError):
    """Raised when an invalid move is attempted"""
    pass

class Tetris:
    def __init__(self):
        try:
            self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
            self.current_piece_type = random.randint(0, get_piece_count() - 1)
            self.current_rotation = 0
            self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
            self.piece_x, self.piece_y = SPAWN_X, SPAWN_Y
            self.fall_time = 0
            
            # Scoring system
            self.score = 0
            self.level = 0
            self.lines_cleared = 0
            self.total_pieces = 0
            
            # Initialize modular UI components
            self.ui = GameUI()
            
            # Keep fonts for backward compatibility (some methods might still use them)
            pygame.font.init()
            self.font = pygame.font.Font(None, 24)
            self.big_font = pygame.font.Font(None, 36)
            self.small_font = pygame.font.Font(None, 18)
            
            logger.info("Tetris game initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Tetris game: {e}")
            raise TetrisError(f"Game initialization failed: {e}")
        
    def new_piece(self):
        """Generate a new random piece"""
        try:
            self.current_piece_type = random.randint(0, get_piece_count() - 1)
            self.current_rotation = 0
            self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
            logger.debug(f"Generated new {get_piece_name(self.current_piece_type)}")
        except (IndexError, ValueError) as e:
            logger.error(f"Failed to generate new piece: {e}")
            # Fallback to T-piece if there's an error
            self.current_piece_type = 0
            self.current_rotation = 0
            self.current_piece = PIECES[0][0]
    
    def valid_move(self, piece, x, y):
        for py, row in enumerate(piece):
            for px, cell in enumerate(row):
                if cell == '#':
                    nx, ny = x + px, y + py
                    # Fixed boundary checks
                    if nx < 0 or nx >= GRID_WIDTH or ny >= GRID_HEIGHT:
                        return False
                    if ny >= 0 and self.grid[ny][nx]:
                        return False
        return True
    
    def place_piece(self):
        """Place current piece on grid and handle scoring"""
        for py, row in enumerate(self.current_piece):
            for px, cell in enumerate(row):
                if cell == '#':
                    if self.piece_y + py >= 0:  # Only place if within bounds
                        # Store piece type + 1 (so 0 remains empty, 1-7 are piece types)
                        self.grid[self.piece_y + py][self.piece_x + px] = self.current_piece_type + 1
        
        # Track pieces placed
        self.total_pieces += 1
        
        self.clear_lines()
        self.new_piece()
        self.piece_x, self.piece_y = SPAWN_X, SPAWN_Y
        
        # Check game over
        if not self.valid_move(self.current_piece, self.piece_x, self.piece_y):
            logger.info(f"Game Over! Final Score: {self.score}, Level: {self.level}, Lines: {self.lines_cleared}")
            self.reset_game()
    
    def reset_game(self):
        """Properly reset game state without reinitializing the object"""
        try:
            self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
            self.current_piece_type = random.randint(0, get_piece_count() - 1)
            self.current_rotation = 0
            self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
            self.piece_x, self.piece_y = SPAWN_X, SPAWN_Y
            self.fall_time = 0
            
            # Reset scoring
            self.score = 0
            self.level = 0
            self.lines_cleared = 0
            self.total_pieces = 0
            
            logger.info("Game reset successfully")
        except Exception as e:
            logger.error(f"Failed to reset game: {e}")
            raise TetrisError(f"Game reset failed: {e}")
    
    def clear_lines(self):
        """Clear completed lines and update score using NES Tetris scoring"""
        lines_cleared = 0
        new_grid = []
        for row in self.grid:
            if 0 in row:  # Keep rows that have empty spaces
                new_grid.append(row)
            else:
                lines_cleared += 1
        
        # Add empty rows at the top
        while len(new_grid) < GRID_HEIGHT:
            new_grid.insert(0, [0 for _ in range(GRID_WIDTH)])
        
        self.grid = new_grid
        
        # Update scoring if lines were cleared
        if lines_cleared > 0:
            self.add_score_for_lines(lines_cleared)
            self.lines_cleared += lines_cleared
            self.update_level()
            
            logger.info(f"Cleared {lines_cleared} lines. Score: {self.score}, Level: {self.level}")
    
    def add_score_for_lines(self, lines_cleared):
        """Add score based on NES Tetris scoring system"""
        base_points = 0
        
        if lines_cleared == 1:
            base_points = Scoring.SINGLE
        elif lines_cleared == 2:
            base_points = Scoring.DOUBLE
        elif lines_cleared == 3:
            base_points = Scoring.TRIPLE
        elif lines_cleared == 4:
            base_points = Scoring.TETRIS
        
        # NES Tetris: Score = base_points * (level + 1)
        points_earned = base_points * (self.level + 1)
        self.score += points_earned
        
        # Log special achievements
        if lines_cleared == 4:
            logger.info(f"TETRIS! Earned {points_earned} points")
        elif lines_cleared >= 2:
            logger.info(f"Multi-line clear! {lines_cleared} lines, {points_earned} points")
    
    def update_level(self):
        """Update level based on lines cleared (NES Tetris style)"""
        new_level = min(self.lines_cleared // Scoring.LINES_PER_LEVEL, Scoring.MAX_LEVEL)
        if new_level > self.level:
            self.level = new_level
            logger.info(f"Level up! Now at level {self.level}")
    
    def get_fall_speed(self):
        """Get current fall speed based on level (NES Tetris speeds)"""
        return Scoring.LEVEL_SPEEDS.get(self.level, Scoring.LEVEL_SPEEDS[29])
    
    def update(self, dt):
        """Update game state with level-based speed"""
        try:
            self.fall_time += dt
            current_fall_speed = self.get_fall_speed()
            
            if self.fall_time >= current_fall_speed:
                if self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
                    self.piece_y += 1
                else:
                    self.place_piece()
                self.fall_time = 0
        except Exception as e:
            logger.error(f"Error in game update: {e}")
            # Continue game execution, don't crash
    
    def move(self, dx):
        if self.valid_move(self.current_piece, self.piece_x + dx, self.piece_y):
            self.piece_x += dx
    
    def rotate(self):
        # Get the number of rotations for current piece
        num_rotations = len(PIECES[self.current_piece_type])
        if num_rotations > 1:  # Only rotate if piece has multiple rotations
            new_rotation = (self.current_rotation + 1) % num_rotations
            new_piece = PIECES[self.current_piece_type][new_rotation]
            
            # Try to rotate in current position
            if self.valid_move(new_piece, self.piece_x, self.piece_y):
                self.current_rotation = new_rotation
                self.current_piece = new_piece
            # Try wall kicks (move left/right to accommodate rotation)
            elif self.valid_move(new_piece, self.piece_x - 1, self.piece_y):
                self.current_rotation = new_rotation
                self.current_piece = new_piece
                self.piece_x -= 1
            elif self.valid_move(new_piece, self.piece_x + 1, self.piece_y):
                self.current_rotation = new_rotation
                self.current_piece = new_piece
                self.piece_x += 1
    
    def drop(self):
        """Soft drop piece and award points"""
        if self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
            self.piece_y += 1
            # Award soft drop points (NES Tetris style)
            self.score += Scoring.SOFT_DROP
    
    def hard_drop(self):
        """Hard drop piece to bottom and award points"""
        try:
            drop_distance = 0
            # Drop piece as far as possible
            while self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
                self.piece_y += 1
                drop_distance += 1
            
            # Award points for hard drop (2 points per cell in NES Tetris)
            hard_drop_points = drop_distance * Scoring.HARD_DROP
            self.score += hard_drop_points
            
            # Log hard drop if significant distance
            if drop_distance > 0:
                logger.debug(f"Hard drop: {drop_distance} cells, {hard_drop_points} points")
            
            # Immediately place the piece since it can't fall further
            self.place_piece()
            self.clear_lines()
            
            # Generate new piece and check for game over (same logic as update method)
            self.new_piece()
            self.piece_x, self.piece_y = SPAWN_X, SPAWN_Y
            
            # Check game over (same logic as existing code)
            if not self.valid_move(self.current_piece, self.piece_x, self.piece_y):
                logger.info(f"Game Over! Final Score: {self.score}, Level: {self.level}, Lines: {self.lines_cleared}")
                self.reset_game()
            
        except Exception as e:
            logger.error(f"Error in hard_drop: {e}")
            # Fallback to regular drop behavior
            self.drop()
    
    def draw(self, screen):
        """Draw the game state using modular UI components"""
        try:
            # Prepare game state for UI components
            game_state = {
                'grid': self.grid,
                'current_piece': self.current_piece,
                'piece_x': self.piece_x,
                'piece_y': self.piece_y,
                'current_piece_type': self.current_piece_type,
                'score': self.score,
                'level': self.level,
                'lines_cleared': self.lines_cleared,
                'total_pieces': self.total_pieces,
                'fall_speed': self.get_fall_speed()
            }
            
            # Draw complete UI using modular components
            self.ui.draw(screen, game_state)
            
        except Exception as e:
            logger.error(f"Error in draw method: {e}")
            # Continue execution, don't crash the game
    
def main():
    """Main game loop with error handling"""
    try:
        game = Tetris()
        running = True
        logger.info("Starting main game loop")
        
        while running:
            try:
                dt = clock.tick(FPS)
                
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        try:
                            if event.key == pygame.K_LEFT:
                                game.move(-1)
                            elif event.key == pygame.K_RIGHT:
                                game.move(1)
                            elif event.key == pygame.K_DOWN:
                                game.drop()
                            elif event.key == pygame.K_UP:
                                game.rotate()
                            elif event.key == pygame.K_SPACE:
                                game.hard_drop()
                        except Exception as e:
                            logger.error(f"Error handling input: {e}")
                
                # Update game state
                game.update(dt)
                
                # Draw everything using modular UI
                game.draw(screen)
                
                pygame.display.flip()
                
            except pygame.error as e:
                logger.error(f"Pygame error in main loop: {e}")
                # Try to continue, but break if it keeps failing
                continue
            except Exception as e:
                logger.error(f"Unexpected error in main loop: {e}")
                continue
                
    except TetrisError as e:
        logger.error(f"Tetris game error: {e}")
        print(f"Game error: {e}")
    except Exception as e:
        logger.error(f"Critical error in main: {e}")
        print(f"Critical error: {e}")
    finally:
        try:
            pygame.quit()
            logger.info("Pygame shut down successfully")
        except Exception as e:
            logger.error(f"Error during pygame shutdown: {e}")
        sys.exit()
    sys.exit()

if __name__ == "__main__":
    main()