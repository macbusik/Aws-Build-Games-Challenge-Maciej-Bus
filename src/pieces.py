"""
Tetris piece definitions and shapes
Contains all 7 standard Tetris pieces with their rotation states and colors
"""

from config import PieceColors

# All 7 Tetris pieces with their rotations - Fixed definitions
# Each piece is defined as a list of rotation states
# Each rotation state is a 5x5 grid where '#' represents a block and '.' represents empty space

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
    # L-piece (SRS Standard - Fixed spawn orientation)
    [
        # State 0 (Spawn) - Horizontal with top-right hook
        ['.....',
         '...#.',
         '.###.',
         '.....',
         '.....'],
        # State R (90° clockwise) - Vertical with bottom-left hook
        ['.....',
         '..#..',
         '..#..',
         '..##.',
         '.....'],
        # State 2 (180°) - Horizontal with bottom-left hook
        ['.....',
         '.....',
         '.###.',
         '.#...',
         '.....'],
        # State L (270° clockwise) - Vertical with top-right hook
        ['.....',
         '.##..',
         '..#..',
         '..#..',
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
    # J-piece (SRS Standard - Fixed spawn orientation)
    [
        # State 0 (Spawn) - Horizontal with top-left hook
        ['.....',
         '.#...',
         '.###.',
         '.....',
         '.....'],
        # State R (90° clockwise) - Vertical with bottom-right hook
        ['.....',
         '..##.',
         '..#..',
         '..#..',
         '.....'],
        # State 2 (180°) - Horizontal with bottom-right hook
        ['.....',
         '.....',
         '.###.',
         '...#.',
         '.....'],
        # State L (270° clockwise) - Vertical with top-left hook
        ['.....',
         '..#..',
         '..#..',
         '.##..',
         '.....']
    ]
]

# Piece type constants for better readability
PIECE_T = 0
PIECE_O = 1
PIECE_L = 2
PIECE_I = 3
PIECE_S = 4
PIECE_Z = 5
PIECE_J = 6

# Piece names for debugging and logging
PIECE_NAMES = {
    PIECE_T: "T-piece",
    PIECE_O: "O-piece", 
    PIECE_L: "L-piece",
    PIECE_I: "I-piece",
    PIECE_S: "S-piece",
    PIECE_Z: "Z-piece",
    PIECE_J: "J-piece"
}

# NES Tetris authentic piece colors mapping
PIECE_COLORS = {
    PIECE_T: PieceColors.T_PIECE,    # Purple
    PIECE_O: PieceColors.O_PIECE,    # Yellow
    PIECE_L: PieceColors.L_PIECE,    # Orange
    PIECE_I: PieceColors.I_PIECE,    # Cyan
    PIECE_S: PieceColors.S_PIECE,    # Green
    PIECE_Z: PieceColors.Z_PIECE,    # Red
    PIECE_J: PieceColors.J_PIECE     # Blue
}

# Border colors for 3D effect
PIECE_BORDER_COLORS = {
    PIECE_T: PieceColors.T_PIECE_BORDER,    # Darker purple
    PIECE_O: PieceColors.O_PIECE_BORDER,    # Darker yellow
    PIECE_L: PieceColors.L_PIECE_BORDER,    # Darker orange
    PIECE_I: PieceColors.I_PIECE_BORDER,    # Darker cyan
    PIECE_S: PieceColors.S_PIECE_BORDER,    # Darker green
    PIECE_Z: PieceColors.Z_PIECE_BORDER,    # Darker red
    PIECE_J: PieceColors.J_PIECE_BORDER     # Darker blue
}

def get_piece_count():
    """Return the total number of piece types"""
    return len(PIECES)

def get_piece_rotations(piece_type):
    """Return the number of rotations for a given piece type"""
    if 0 <= piece_type < len(PIECES):
        return len(PIECES[piece_type])
    return 0

def get_piece_name(piece_type):
    """Return the name of a piece type"""
    return PIECE_NAMES.get(piece_type, f"Unknown piece {piece_type}")

def get_piece_color(piece_type):
    """Return the color for a piece type"""
    return PIECE_COLORS.get(piece_type, PieceColors.T_PIECE)

def get_piece_border_color(piece_type):
    """Return the border color for a piece type"""
    return PIECE_BORDER_COLORS.get(piece_type, PieceColors.T_PIECE_BORDER)

def validate_piece_definitions():
    """Validate that all piece definitions are correct"""
    errors = []
    
    # Check we have exactly 7 pieces
    if len(PIECES) != 7:
        errors.append(f"Expected 7 pieces, found {len(PIECES)}")
    
    # Check each piece
    for i, piece in enumerate(PIECES):
        piece_name = get_piece_name(i)
        
        # Check piece has at least one rotation
        if not piece:
            errors.append(f"{piece_name}: No rotations defined")
            continue
            
        # Check each rotation
        for j, rotation in enumerate(piece):
            # Check rotation is 5x5
            if len(rotation) != 5:
                errors.append(f"{piece_name} rotation {j}: Expected 5 rows, found {len(rotation)}")
                continue
                
            for k, row in enumerate(rotation):
                if len(row) != 5:
                    errors.append(f"{piece_name} rotation {j} row {k}: Expected 5 columns, found {len(row)}")
                
                # Check only valid characters
                for char in row:
                    if char not in '.#':
                        errors.append(f"{piece_name} rotation {j} row {k}: Invalid character '{char}'")
            
            # Check exactly 4 blocks per rotation
            block_count = sum(row.count('#') for row in rotation)
            if block_count != 4:
                errors.append(f"{piece_name} rotation {j}: Expected 4 blocks, found {block_count}")
    
    # Check color mappings
    for piece_type in range(get_piece_count()):
        if piece_type not in PIECE_COLORS:
            errors.append(f"Missing color for piece type {piece_type}")
        if piece_type not in PIECE_BORDER_COLORS:
            errors.append(f"Missing border color for piece type {piece_type}")
    
    return errors

# Validate pieces on import
_validation_errors = validate_piece_definitions()
if _validation_errors:
    raise ValueError(f"Piece definition errors: {_validation_errors}")
