"""
Configuration constants for Tetris game
"""

# Display settings
WINDOW_WIDTH = 550  # Increased to accommodate score display
WINDOW_HEIGHT = 600
BLOCK_SIZE = 30

# Grid settings
GRID_WIDTH = 10
GRID_HEIGHT = 20

# Game mechanics
FALL_SPEED_MS = 500
SPAWN_X = 3
SPAWN_Y = 0

# Frame rate
FPS = 60

# Scoring system (NES Tetris compatible)
class Scoring:
    # Line clear points (multiplied by level + 1)
    SINGLE = 40      # 1 line
    DOUBLE = 100     # 2 lines  
    TRIPLE = 300     # 3 lines
    TETRIS = 1200    # 4 lines (Tetris!)
    
    # Soft drop points
    SOFT_DROP = 1    # Per cell dropped
    
    # Hard drop points  
    HARD_DROP = 2    # Per cell hard dropped (space bar)
    
    # Level progression
    LINES_PER_LEVEL = 10
    MAX_LEVEL = 29
    
    # Speed progression (fall speed in milliseconds)
    LEVEL_SPEEDS = {
        0: 800, 1: 717, 2: 633, 3: 550, 4: 467, 5: 383,
        6: 300, 7:217, 8: 133, 9: 100, 10: 83, 11: 83,
        12: 83, 13: 67, 14: 67, 15: 67, 16: 50, 17: 50,
        18: 50, 19: 33, 20: 33, 21: 33, 22: 33, 23: 33,
        24: 33, 25: 33, 26: 33, 27: 33, 28: 33, 29: 17
    }

# Colors (RGB tuples)
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    CYAN = (0, 255, 255)
    GRAY = (128, 128, 128)
    DARK_GRAY = (64, 64, 64)
    LIGHT_GRAY = (192, 192, 192)

# NES Tetris authentic piece colors
class PieceColors:
    """Authentic NES Tetris piece colors"""
    T_PIECE = (128, 0, 128)    # Purple/Magenta
    O_PIECE = (255, 255, 0)    # Yellow  
    L_PIECE = (255, 165, 0)    # Orange
    I_PIECE = (0, 255, 255)    # Cyan/Light Blue
    S_PIECE = (0, 255, 0)      # Green
    Z_PIECE = (255, 0, 0)      # Red
    J_PIECE = (0, 0, 255)      # Blue
    
    # Border colors (slightly darker for 3D effect)
    T_PIECE_BORDER = (96, 0, 96)      # Darker purple
    O_PIECE_BORDER = (192, 192, 0)    # Darker yellow
    L_PIECE_BORDER = (192, 124, 0)    # Darker orange
    I_PIECE_BORDER = (0, 192, 192)    # Darker cyan
    S_PIECE_BORDER = (0, 192, 0)      # Darker green
    Z_PIECE_BORDER = (192, 0, 0)      # Darker red
    J_PIECE_BORDER = (0, 0, 192)      # Darker blue
    
    # Grid colors
    GRID_BACKGROUND = (32, 32, 32)    # Dark gray background
    GRID_BORDER = (96, 96, 96)        # Medium gray borders
    EMPTY_CELL = (16, 16, 16)         # Very dark gray for empty cells

# Game title
GAME_TITLE = "Tetris - AWS Build Games Challenge"
