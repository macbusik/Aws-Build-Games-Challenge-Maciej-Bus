"""
UI Components for Tetris Game
Modular design with separate components for better organization
"""

import pygame
import logging
from config import *
from pieces import PieceColors

logger = logging.getLogger(__name__)

class GameField:
    """Game field component - handles the main playing area with grid"""
    
    def __init__(self, x=0, y=0):
        """Initialize game field at specified position"""
        self.x = x
        self.y = y
        self.width = GRID_WIDTH * BLOCK_SIZE
        self.height = GRID_HEIGHT * BLOCK_SIZE
        
        # Initialize fonts for any text in game field
        pygame.font.init()
        self.font = pygame.font.Font(None, 24)
        
    def draw_background(self, screen):
        """Draw the game field background"""
        try:
            # Draw background rectangle for game field
            game_rect = pygame.Rect(self.x, self.y, self.width, self.height)
            pygame.draw.rect(screen, PieceColors.GRID_BACKGROUND, game_rect)
            
            # Draw border around game field
            pygame.draw.rect(screen, PieceColors.GRID_BORDER, game_rect, 2)
            
        except Exception as e:
            logger.error(f"Error drawing game field background: {e}")
    
    def draw_grid_lines(self, screen):
        """Draw grid lines only within the game field"""
        try:
            # Draw vertical lines (only within game field)
            for x in range(GRID_WIDTH + 1):
                line_x = self.x + (x * BLOCK_SIZE)
                pygame.draw.line(screen, PieceColors.GRID_BORDER,
                               (line_x, self.y),
                               (line_x, self.y + self.height), 1)
            
            # Draw horizontal lines (only within game field)
            for y in range(GRID_HEIGHT + 1):
                line_y = self.y + (y * BLOCK_SIZE)
                pygame.draw.line(screen, PieceColors.GRID_BORDER,
                               (self.x, line_y),
                               (self.x + self.width, line_y), 1)
                               
        except Exception as e:
            logger.error(f"Error drawing game field grid: {e}")
    
    def draw_pieces(self, screen, grid, current_piece, piece_x, piece_y, current_piece_type):
        """Draw placed pieces and current piece within game field"""
        try:
            # Import here to avoid circular imports
            from pieces import get_piece_color, get_piece_border_color
            
            # Draw placed pieces
            for y in range(GRID_HEIGHT):
                for x in range(GRID_WIDTH):
                    if grid[y][x] != 0:
                        piece_type = grid[y][x] - 1
                        color = get_piece_color(piece_type)
                        border_color = get_piece_border_color(piece_type)
                        
                        # Calculate position within game field
                        block_x = self.x + (x * BLOCK_SIZE)
                        block_y = self.y + (y * BLOCK_SIZE)
                        
                        # Draw 3D block effect
                        pygame.draw.rect(screen, color, 
                                       (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))
                        pygame.draw.rect(screen, border_color, 
                                       (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE), 2)
            
            # Draw current falling piece
            if current_piece:
                current_color = get_piece_color(current_piece_type)
                current_border = get_piece_border_color(current_piece_type)
                
                for py, row in enumerate(current_piece):
                    for px, cell in enumerate(row):
                        if cell == '#':
                            # Calculate position within game field
                            block_x = self.x + ((piece_x + px) * BLOCK_SIZE)
                            block_y = self.y + ((piece_y + py) * BLOCK_SIZE)
                            
                            # Only draw if within game field bounds
                            if (0 <= piece_x + px < GRID_WIDTH and 
                                0 <= piece_y + py < GRID_HEIGHT):
                                
                                # Draw 3D block effect
                                pygame.draw.rect(screen, current_color, 
                                               (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE))
                                pygame.draw.rect(screen, current_border, 
                                               (block_x, block_y, BLOCK_SIZE, BLOCK_SIZE), 2)
                                               
        except Exception as e:
            logger.error(f"Error drawing pieces in game field: {e}")
    
    def draw(self, screen, grid, current_piece, piece_x, piece_y, current_piece_type):
        """Draw complete game field"""
        self.draw_background(screen)
        self.draw_grid_lines(screen)
        self.draw_pieces(screen, grid, current_piece, piece_x, piece_y, current_piece_type)


class ScoreBoard:
    """Score board component - handles score, level, lines display"""
    
    def __init__(self, x, y, width=200):
        """Initialize score board at specified position"""
        self.x = x
        self.y = y
        self.width = width
        self.height = 400  # Enough space for all score info
        
        # Initialize fonts
        pygame.font.init()
        self.font = pygame.font.Font(None, 24)
        self.big_font = pygame.font.Font(None, 36)
        
    def draw_background(self, screen):
        """Draw score board background"""
        try:
            # Draw subtle background for score area
            score_rect = pygame.Rect(self.x - 5, self.y - 5, self.width + 10, self.height + 10)
            pygame.draw.rect(screen, (20, 20, 20), score_rect)
            pygame.draw.rect(screen, Colors.DARK_GRAY, score_rect, 1)
            
        except Exception as e:
            logger.error(f"Error drawing score board background: {e}")
    
    def draw_score_info(self, screen, score, level, lines_cleared, total_pieces, fall_speed):
        """Draw all score information"""
        try:
            current_y = self.y
            
            # Score
            score_text = self.font.render("SCORE", True, Colors.WHITE)
            score_value = self.big_font.render(f"{score:08d}", True, Colors.YELLOW)
            screen.blit(score_text, (self.x, current_y))
            screen.blit(score_value, (self.x, current_y + 20))
            current_y += 70
            
            # Level
            level_text = self.font.render("LEVEL", True, Colors.WHITE)
            level_value = self.big_font.render(f"{level}", True, Colors.CYAN)
            screen.blit(level_text, (self.x, current_y))
            screen.blit(level_value, (self.x, current_y + 20))
            current_y += 70
            
            # Lines
            lines_text = self.font.render("LINES", True, Colors.WHITE)
            lines_value = self.big_font.render(f"{lines_cleared}", True, Colors.GREEN)
            screen.blit(lines_text, (self.x, current_y))
            screen.blit(lines_value, (self.x, current_y + 20))
            current_y += 70
            
            # Pieces (bonus info)
            pieces_text = self.font.render("PIECES", True, Colors.WHITE)
            pieces_value = self.font.render(f"{total_pieces}", True, Colors.LIGHT_GRAY)
            screen.blit(pieces_text, (self.x, current_y))
            screen.blit(pieces_value, (self.x, current_y + 20))
            current_y += 50
            
            # Speed indicator
            speed_text = self.font.render("SPEED", True, Colors.WHITE)
            speed_value = self.font.render(f"{fall_speed}ms", True, Colors.LIGHT_GRAY)
            screen.blit(speed_text, (self.x, current_y))
            screen.blit(speed_value, (self.x, current_y + 20))
            
        except Exception as e:
            logger.error(f"Error drawing score info: {e}")
    
    def draw(self, screen, score, level, lines_cleared, total_pieces, fall_speed):
        """Draw complete score board"""
        self.draw_background(screen)
        self.draw_score_info(screen, score, level, lines_cleared, total_pieces, fall_speed)


class HowToPlayPanel:
    """How-to-play panel component - handles instruction display"""
    
    def __init__(self, x, y, width=540):
        """Initialize how-to-play panel at specified position"""
        self.x = x
        self.y = y
        self.width = width
        self.height = 140  # Compact height for instructions
        
        # Initialize fonts
        pygame.font.init()
        self.font = pygame.font.Font(None, 24)
        self.small_font = pygame.font.Font(None, 18)
        
    def draw_background(self, screen):
        """Draw how-to-play panel background"""
        try:
            # Draw subtle background for instructions
            panel_rect = pygame.Rect(self.x - 5, self.y - 5, self.width + 10, self.height + 10)
            pygame.draw.rect(screen, (15, 15, 15), panel_rect)
            pygame.draw.rect(screen, Colors.DARK_GRAY, panel_rect, 1)
            
        except Exception as e:
            logger.error(f"Error drawing how-to-play background: {e}")
    
    def draw_instructions(self, screen):
        """Draw how-to-play instructions"""
        try:
            current_y = self.y
            
            # Title
            title_text = self.font.render("HOW TO PLAY", True, Colors.YELLOW)
            screen.blit(title_text, (self.x, current_y))
            current_y += 25
            
            # Controls section
            controls_title = self.small_font.render("CONTROLS:", True, Colors.WHITE)
            screen.blit(controls_title, (self.x, current_y))
            
            # Control instructions
            controls = [
                "[LEFT] [RIGHT] - Move pieces",
                "[UP] - Rotate pieces", 
                "[DOWN] - Soft drop (+1pt/cell)",
                "[SPACE] - Hard drop (+2pt/cell)",
            ]
            
            for i, control in enumerate(controls):
                control_text = self.small_font.render(control, True, Colors.LIGHT_GRAY)
                screen.blit(control_text, (self.x, current_y + 15 + (i * 14)))
            
            # Scoring section (positioned to the right of controls)
            scoring_x = self.x + 240
            scoring_title = self.small_font.render("SCORING:", True, Colors.WHITE)
            screen.blit(scoring_title, (scoring_x, current_y))
            
            # Scoring instructions
            scoring = [
                "1 line = 40 x (level+1)",
                "2 lines = 100 x (level+1)",
                "3 lines = 300 x (level+1)", 
                "4 lines = 1200 x (level+1) TETRIS!",
                "Level up every 10 lines"
            ]
            
            for i, score in enumerate(scoring):
                score_text = self.small_font.render(score, True, Colors.LIGHT_GRAY)
                screen.blit(score_text, (scoring_x, current_y + 15 + (i * 14)))
                
        except Exception as e:
            logger.error(f"Error drawing instructions: {e}")
    
    def draw(self, screen):
        """Draw complete how-to-play panel"""
        self.draw_background(screen)
        self.draw_instructions(screen)


class GameUI:
    """Main UI coordinator - manages all UI components"""
    
    def __init__(self):
        """Initialize all UI components with proper positioning"""
        # Game field positioned at top-left
        self.game_field = GameField(x=10, y=10)
        
        # Score board positioned to the right of game field
        score_x = self.game_field.x + self.game_field.width + 20
        self.score_board = ScoreBoard(x=score_x, y=20)
        
        # How-to-play panel positioned below game field
        help_y = self.game_field.y + self.game_field.height + 20
        self.how_to_play = HowToPlayPanel(x=10, y=help_y)
        
    def draw_background(self, screen):
        """Draw main window background"""
        screen.fill(Colors.BLACK)
    
    def draw(self, screen, game_state):
        """Draw complete UI with all components"""
        try:
            # Draw main background
            self.draw_background(screen)
            
            # Draw game field with pieces
            self.game_field.draw(screen, 
                                game_state['grid'], 
                                game_state['current_piece'],
                                game_state['piece_x'], 
                                game_state['piece_y'],
                                game_state['current_piece_type'])
            
            # Draw score board
            self.score_board.draw(screen,
                                 game_state['score'],
                                 game_state['level'],
                                 game_state['lines_cleared'],
                                 game_state['total_pieces'],
                                 game_state['fall_speed'])
            
            # Draw how-to-play panel
            self.how_to_play.draw(screen)
            
        except Exception as e:
            logger.error(f"Error drawing game UI: {e}")
