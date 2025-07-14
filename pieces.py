"""
Tetris piece definitions and shapes
Contains all 7 standard Tetris pieces with their rotation states
"""

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
    
    return errors

# Validate pieces on import
_validation_errors = validate_piece_definitions()
if _validation_errors:
    raise ValueError(f"Piece definition errors: {_validation_errors}")
