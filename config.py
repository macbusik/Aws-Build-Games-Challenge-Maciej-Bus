"""
Configuration constants for Tetris game
"""

# Display settings
WINDOW_WIDTH = 400
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

# Game title
GAME_TITLE = "Tetris - AWS Build Games Challenge"
