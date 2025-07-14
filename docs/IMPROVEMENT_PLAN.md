# Tetris Code Improvement Implementation Plan

## 🎯 Phase 1: Critical Fixes (High Priority)

### 1.1 Fix Game Reset Mechanism
**Current Issue**: Using `self.__init__()` for game reset is dangerous
```python
# ❌ Current problematic code
if not self.valid_move(self.current_piece, self.piece_x, self.piece_y):
    self.__init__()  # This can cause issues
```

**✅ Proposed Fix**:
```python
def reset_game(self):
    """Properly reset game state without reinitializing the object"""
    self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    self.current_piece_type = random.randint(0, len(PIECES) - 1)
    self.current_rotation = 0
    self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
    self.piece_x, self.piece_y = 3, 0
    self.fall_time = 0
    self.game_over = False

def check_game_over(self):
    """Check if game is over and handle it properly"""
    if not self.valid_move(self.current_piece, self.piece_x, self.piece_y):
        self.game_over = True
        return True
    return False
```

### 1.2 Extract Constants and Configuration
**✅ Create config.py**:
```python
# config.py
from typing import Tuple
from enum import Enum

class GameConfig:
    # Display settings
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 600
    BLOCK_SIZE = 30
    
    # Grid settings
    GRID_WIDTH = 10
    GRID_HEIGHT = 20
    
    # Game mechanics
    FALL_SPEED_MS = 500
    SPAWN_X = GRID_WIDTH // 2 - 1
    SPAWN_Y = 0
    
    # Frame rate
    FPS = 60

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

class PieceType(Enum):
    T = 0
    O = 1
    L = 2
    I = 3
    S = 4
    Z = 5
    J = 6

# Piece colors mapping
PIECE_COLORS = {
    PieceType.T: Colors.PURPLE,
    PieceType.O: Colors.YELLOW,
    PieceType.L: Colors.ORANGE,
    PieceType.I: Colors.CYAN,
    PieceType.S: Colors.GREEN,
    PieceType.Z: Colors.RED,
    PieceType.J: Colors.BLUE,
}
```

### 1.3 Add Error Handling
**✅ Proposed improvements**:
```python
import logging
from typing import Optional, List, Tuple

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TetrisError(Exception):
    """Base exception for Tetris game errors"""
    pass

class InvalidMoveError(TetrisError):
    """Raised when an invalid move is attempted"""
    pass

class GameInitializationError(TetrisError):
    """Raised when game fails to initialize"""
    pass
```

## 🏗️ Phase 2: Code Structure Refactoring (Medium Priority)

### 2.1 Separate Piece Management
**✅ Create pieces.py**:
```python
# pieces.py
from typing import List, Dict
from config import PieceType
from dataclasses import dataclass

@dataclass
class Piece:
    shape: List[List[str]]
    type: PieceType
    rotation: int = 0
    x: int = 0
    y: int = 0

class PieceManager:
    """Manages Tetris pieces and their rotations"""
    
    def __init__(self):
        self.pieces_data = PIECES  # Move PIECES constant here
    
    def get_piece(self, piece_type: PieceType, rotation: int = 0) -> List[List[str]]:
        """Get piece shape for given type and rotation"""
        try:
            return self.pieces_data[piece_type.value][rotation]
        except IndexError:
            logger.error(f"Invalid piece type {piece_type} or rotation {rotation}")
            raise InvalidMoveError(f"Invalid piece configuration")
    
    def get_random_piece(self) -> Piece:
        """Generate a random piece"""
        piece_type = PieceType(random.randint(0, len(PieceType) - 1))
        shape = self.get_piece(piece_type)
        return Piece(shape=shape, type=piece_type, x=GameConfig.SPAWN_X, y=GameConfig.SPAWN_Y)
    
    def rotate_piece(self, piece: Piece) -> Piece:
        """Return rotated version of piece"""
        max_rotations = len(self.pieces_data[piece.type.value])
        if max_rotations <= 1:
            return piece
        
        new_rotation = (piece.rotation + 1) % max_rotations
        new_shape = self.get_piece(piece.type, new_rotation)
        
        return Piece(
            shape=new_shape,
            type=piece.type,
            rotation=new_rotation,
            x=piece.x,
            y=piece.y
        )
```

### 2.2 Separate Rendering Logic
**✅ Create renderer.py**:
```python
# renderer.py
import pygame
from typing import List, Optional
from config import GameConfig, Colors, PIECE_COLORS
from pieces import Piece

class GameRenderer:
    """Handles all game rendering operations"""
    
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
    
    def draw_grid(self, grid: List[List[int]]):
        """Draw the game grid"""
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    self._draw_block(x, y, Colors.WHITE)
    
    def draw_piece(self, piece: Piece):
        """Draw a single piece"""
        color = PIECE_COLORS.get(piece.type, Colors.RED)
        
        for py, row in enumerate(piece.shape):
            for px, cell in enumerate(row):
                if cell == '#':
                    self._draw_block(piece.x + px, piece.y + py, color)
    
    def draw_grid_lines(self):
        """Draw grid lines for better visibility"""
        for x in range(GameConfig.GRID_WIDTH + 1):
            pygame.draw.line(
                self.screen, 
                Colors.DARK_GRAY,
                (x * GameConfig.BLOCK_SIZE, 0),
                (x * GameConfig.BLOCK_SIZE, GameConfig.WINDOW_HEIGHT)
            )
        
        for y in range(GameConfig.GRID_HEIGHT + 1):
            pygame.draw.line(
                self.screen,
                Colors.DARK_GRAY,
                (0, y * GameConfig.BLOCK_SIZE),
                (GameConfig.WINDOW_WIDTH, y * GameConfig.BLOCK_SIZE)
            )
    
    def draw_score(self, score: int, level: int, lines: int):
        """Draw score information"""
        score_text = self.font.render(f"Score: {score}", True, Colors.WHITE)
        level_text = self.font.render(f"Level: {level}", True, Colors.WHITE)
        lines_text = self.font.render(f"Lines: {lines}", True, Colors.WHITE)
        
        # Position these on the right side or top
        # Implementation depends on UI layout
    
    def draw_game_over(self):
        """Draw game over screen"""
        overlay = pygame.Surface((GameConfig.WINDOW_WIDTH, GameConfig.WINDOW_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(Colors.BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = self.font.render("GAME OVER", True, Colors.WHITE)
        text_rect = game_over_text.get_rect(
            center=(GameConfig.WINDOW_WIDTH // 2, GameConfig.WINDOW_HEIGHT // 2)
        )
        self.screen.blit(game_over_text, text_rect)
    
    def _draw_block(self, x: int, y: int, color: tuple, border_color: Optional[tuple] = None):
        """Draw a single block with optional border"""
        rect = pygame.Rect(
            x * GameConfig.BLOCK_SIZE,
            y * GameConfig.BLOCK_SIZE,
            GameConfig.BLOCK_SIZE,
            GameConfig.BLOCK_SIZE
        )
        
        pygame.draw.rect(self.screen, color, rect)
        
        if border_color:
            pygame.draw.rect(self.screen, border_color, rect, 1)
```

## 🎮 Phase 3: Game Features Enhancement (Medium Priority)

### 3.1 Add Game State Management
**✅ Create game_state.py**:
```python
# game_state.py
from enum import Enum
from dataclasses import dataclass

class GameState(Enum):
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"

@dataclass
class GameStats:
    score: int = 0
    level: int = 1
    lines_cleared: int = 0
    total_pieces: int = 0
    
    def add_lines(self, lines: int):
        """Add cleared lines and update level"""
        self.lines_cleared += lines
        self.level = min(10, self.lines_cleared // 10 + 1)
        
        # Scoring system (standard Tetris scoring)
        line_scores = {1: 40, 2: 100, 3: 300, 4: 1200}
        self.score += line_scores.get(lines, 0) * self.level
```

### 3.2 Enhanced Game Logic
**✅ Improved main game class**:
```python
# game.py
from typing import Optional
import pygame
import random
from config import GameConfig, GameState
from pieces import PieceManager, Piece
from renderer import GameRenderer
from game_state import GameStats

class TetrisGame:
    """Main Tetris game class with improved architecture"""
    
    def __init__(self):
        self.grid = [[0 for _ in range(GameConfig.GRID_WIDTH)] 
                    for _ in range(GameConfig.GRID_HEIGHT)]
        
        self.piece_manager = PieceManager()
        self.current_piece: Optional[Piece] = None
        self.next_piece: Optional[Piece] = None
        self.stats = GameStats()
        self.state = GameState.PLAYING
        self.fall_time = 0
        
        # Initialize pieces
        self._spawn_new_piece()
        self._generate_next_piece()
    
    def _spawn_new_piece(self):
        """Spawn a new piece"""
        if self.next_piece:
            self.current_piece = self.next_piece
            self._generate_next_piece()
        else:
            self.current_piece = self.piece_manager.get_random_piece()
        
        self.stats.total_pieces += 1
        
        # Check game over
        if not self._is_valid_position(self.current_piece):
            self.state = GameState.GAME_OVER
    
    def _generate_next_piece(self):
        """Generate next piece for preview"""
        self.next_piece = self.piece_manager.get_random_piece()
    
    def update(self, dt: int):
        """Update game state"""
        if self.state != GameState.PLAYING:
            return
        
        self.fall_time += dt
        fall_speed = max(50, GameConfig.FALL_SPEED_MS - (self.stats.level - 1) * 50)
        
        if self.fall_time >= fall_speed:
            self._try_move_piece(0, 1)
            self.fall_time = 0
    
    def _try_move_piece(self, dx: int, dy: int) -> bool:
        """Try to move current piece"""
        if not self.current_piece:
            return False
        
        new_piece = Piece(
            shape=self.current_piece.shape,
            type=self.current_piece.type,
            rotation=self.current_piece.rotation,
            x=self.current_piece.x + dx,
            y=self.current_piece.y + dy
        )
        
        if self._is_valid_position(new_piece):
            self.current_piece = new_piece
            return True
        elif dy > 0:  # Piece hit bottom
            self._place_piece()
            return False
        
        return False
```

## 📋 Implementation Priority

### Week 1: Critical Fixes
- [ ] Fix game reset mechanism
- [ ] Extract constants to config files
- [ ] Add basic error handling
- [ ] Update unit tests

### Week 2: Structure Refactoring  
- [ ] Create separate modules (config, pieces, renderer)
- [ ] Refactor main game class
- [ ] Add type hints and docstrings
- [ ] Update tests for new structure

### Week 3: Feature Enhancement
- [ ] Add scoring system
- [ ] Implement game states
- [ ] Add next piece preview
- [ ] Implement pause functionality

### Week 4: Polish & Testing
- [ ] Performance optimization
- [ ] Comprehensive testing
- [ ] Documentation updates
- [ ] Code review and cleanup

## 🧪 Testing Strategy

### Unit Tests to Add:
```python
# test_pieces.py
def test_piece_rotation_validity()
def test_piece_color_mapping()
def test_random_piece_generation()

# test_game_logic.py  
def test_scoring_system()
def test_level_progression()
def test_game_state_transitions()

# test_renderer.py
def test_block_drawing()
def test_score_display()
def test_game_over_screen()
```

This plan provides a structured approach to improving the codebase while maintaining functionality throughout the process.
