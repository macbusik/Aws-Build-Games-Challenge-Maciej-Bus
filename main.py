import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 400, 600
BLOCK_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = 10, 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

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
    # L-piece (Correctly Fixed)
    [
        ['.....',
         '..#..',
         '..#..',
         '..##.',
         '.....'],
        ['.....',
         '.....',
         '.###.',
         '...#.',
         '.....'],
        ['.....',
         '.##..',
         '..#..',
         '..#..',
         '.....'],
        ['.....',
         '.....',
         '.#...',
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
    # J-piece (Correctly Fixed)
    [
        ['.....',
         '.#...',
         '.#...',
         '.##..',
         '.....'],
        ['.....',
         '.....',
         '.#...',
         '.###.',
         '.....'],
        ['.....',
         '.##..',
         '.#...',
         '.#...',
         '.....'],
        ['.....',
         '.....',
         '.###.',
         '...#.',
         '.....']
    ]
]

class Tetris:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece_type = random.randint(0, len(PIECES) - 1)
        self.current_rotation = 0
        self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
        self.piece_x, self.piece_y = 3, 0
        self.fall_time = 0
        
    def new_piece(self):
        self.current_piece_type = random.randint(0, len(PIECES) - 1)
        self.current_rotation = 0
        self.current_piece = PIECES[self.current_piece_type][self.current_rotation]
    
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
        self.piece_x, self.piece_y = 3, 0
        
        # Check game over
        if not self.valid_move(self.current_piece, self.piece_x, self.piece_y):
            self.__init__()  # Reset game
    
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
        self.fall_time += dt
        if self.fall_time >= 500:
            if self.valid_move(self.current_piece, self.piece_x, self.piece_y + 1):
                self.piece_y += 1
            else:
                self.place_piece()
            self.fall_time = 0
    
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
        # Draw grid
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, (255, 255, 255), 
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, (128, 128, 128), 
                                   (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        
        # Draw current piece
        for py, row in enumerate(self.current_piece):
            for px, cell in enumerate(row):
                if cell == '#':
                    pygame.draw.rect(screen, (255, 0, 0), 
                                   ((self.piece_x + px) * BLOCK_SIZE, 
                                    (self.piece_y + py) * BLOCK_SIZE, 
                                    BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.rect(screen, (128, 0, 0), 
                                   ((self.piece_x + px) * BLOCK_SIZE, 
                                    (self.piece_y + py) * BLOCK_SIZE, 
                                    BLOCK_SIZE, BLOCK_SIZE), 1)

def main():
    game = Tetris()
    running = True
    
    while running:
        dt = clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1)
                elif event.key == pygame.K_RIGHT:
                    game.move(1)
                elif event.key == pygame.K_DOWN:
                    game.drop()
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    game.rotate()
        
        game.update(dt)
        
        screen.fill((0, 0, 0))
        game.draw(screen)
        
        # Draw grid lines for better visibility
        for x in range(GRID_WIDTH + 1):
            pygame.draw.line(screen, (64, 64, 64), 
                           (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, HEIGHT))
        for y in range(GRID_HEIGHT + 1):
            pygame.draw.line(screen, (64, 64, 64), 
                           (0, y * BLOCK_SIZE), (WIDTH, y * BLOCK_SIZE))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()