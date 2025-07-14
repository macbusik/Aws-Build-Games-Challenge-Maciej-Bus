import pygame
import random
import sys
import logging
from config import *

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

# Tetris pieces with all rotations - Fixed definitions
PIECES = [
    # T-piece
    [
        ['.....',
         '..#..',
         '.###.',
         '.....',
         '.....'],
        ['.....',
         '..#..',
         '..##.',
         '..#..',
         '.....'],
        ['.....',
         '.....',
         '.###.',
         '..#..',
         '.....'],
        ['.....',
         '..#..',
         '.##..',
         '..#..',
         '.....']
    ],
    # O-piece (square)
    [
        ['.....',
         '.....',
         '.##..',
         '.##..',
         '.....']
    ],
    # L-piece (CORRECTLY Fixed)
    [
        ['.....',
         '..#..',
         '..#..',
         '..##.',
         '.....'],
        ['.....',
         '.....',
         '.###.',
         '.#...',
         '.....'],
        ['.....',
         '.##..',
         '..#..',
         '..#..',
         '.....'],
        ['.....',
         '.....',
         '...#.',
         '.###.',
         '.....']
    ],
    # I-piece (Fixed)
    [
        ['.....',
         '.....',
         '####.',
         '.....',
         '.....'],
        ['.....',
         '..#..',
         '..#..',
         '..#..',
         '..#..']
    ],
    # S-piece
    [
        ['.....',
         '.....',
         '.##..',
         '##...',
         '.....'],
        ['.....',
         '.#...',
         '.##..',
         '..#..',
         '.....']
    ],
    # Z-piece
    [
        ['.....',
         '.....',
         '##...',
         '.##..',
         '.....'],
        ['.....',
         '..#..',
         '.##..',
         '.#...',
         '.....']
    ],
    # J-piece (CORRECTLY Fixed)
    [
        ['.....',
         '.#...',
         '.#...',
         '.##..',
         '.....'],
        ['.....',
         '.#...',
         '.###.',
         '.....',
         '.....'],
        ['.....',
         '.##..',
         '.#...',
         '.#...',
         '.....'],
        ['.....',
         '.....',
         '.###.',
         '.#...',
         '.....']
    ]
]

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
            self.current_piece_type = random.randint(0, len(PIECES) - 1)
            self.current_rotation = 0
            self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
            self.piece_x, self.piece_y = SPAWN_X, SPAWN_Y
            self.fall_time = 0
            logger.info("Tetris game initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize Tetris game: {e}")
            raise TetrisError(f"Game initialization failed: {e}")
        
    def new_piece(self):
        """Generate a new random piece"""
        try:
            self.current_piece_type = random.randint(0, len(PIECES) - 1)
            self.current_rotation = 0
            self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
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
        for py, row in enumerate(self.current_piece):
            for px, cell in enumerate(row):
                if cell == '#':
                    if self.piece_y + py >= 0:  # Only place if within bounds
                        self.grid[self.piece_y + py][self.piece_x + px] = 1
        self.clear_lines()
        self.new_piece()
        self.piece_x, self.piece_y = SPAWN_X, SPAWN_Y
        
        # Check game over
        if not self.valid_move(self.current_piece, self.piece_x, self.piece_y):
            self.reset_game()
    
    def reset_game(self):
        """Properly reset game state without reinitializing the object"""
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece_type = random.randint(0, len(PIECES) - 1)
        self.current_rotation = 0
        self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
        self.piece_x, self.piece_y = SPAWN_X, SPAWN_Y
        self.fall_time = 0
    
    def clear_lines(self):
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
    
    def update(self, dt):
        """Update game state"""
        try:
            self.fall_time += dt
            if self.fall_time >= FALL_SPEED_MS:
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
        if self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
            self.piece_y += 1
    
    def draw(self, screen):
        """Draw the game state to screen"""
        try:
            # Draw grid
            for y, row in enumerate(self.grid):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(screen, Colors.WHITE, 
                                       (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(screen, Colors.GRAY, 
                                       (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
            
            # Draw current piece
            for py, row in enumerate(self.current_piece):
                for px, cell in enumerate(row):
                    if cell == '#':
                        pygame.draw.rect(screen, Colors.RED, 
                                       ((self.piece_x + px) * BLOCK_SIZE, 
                                        (self.piece_y + py) * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(screen, Colors.DARK_GRAY, 
                                       ((self.piece_x + px) * BLOCK_SIZE, 
                                        (self.piece_y + py) * BLOCK_SIZE, 
                                        BLOCK_SIZE, BLOCK_SIZE), 1)
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
                            elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                                game.rotate()
                        except Exception as e:
                            logger.error(f"Error handling input: {e}")
                
                # Update game state
                game.update(dt)
                
                # Draw everything
                screen.fill(Colors.BLACK)
                game.draw(screen)
                
                # Draw grid lines for better visibility
                for x in range(GRID_WIDTH + 1):
                    pygame.draw.line(screen, Colors.DARK_GRAY, 
                                   (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, WINDOW_HEIGHT))
                for y in range(GRID_HEIGHT + 1):
                    pygame.draw.line(screen, Colors.DARK_GRAY, 
                                   (0, y * BLOCK_SIZE), (WINDOW_WIDTH, y * BLOCK_SIZE))
                
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