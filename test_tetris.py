import unittest
import sys
import os

# Add the current directory to the path so we can import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import Tetris, PIECES, GRID_WIDTH, GRID_HEIGHT

class TestTetrisPieces(unittest.TestCase):
    """Test Tetris piece definitions and rotations"""
    
    def setUp(self):
        self.game = Tetris()
    
    def test_piece_count(self):
        """Test that we have all 7 standard Tetris pieces"""
        self.assertEqual(len(PIECES), 7, "Should have 7 Tetris pieces")
    
    def test_t_piece_rotations(self):
        """Test T-piece has 4 rotations and correct shape"""
        t_piece = PIECES[0]  # T-piece
        self.assertEqual(len(t_piece), 4, "T-piece should have 4 rotations")
        
        # Test first rotation (upward T)
        first_rotation = t_piece[0]
        self.assertIn('..#..', first_rotation[1])
        self.assertIn('.###.', first_rotation[2])
    
    def test_o_piece_rotations(self):
        """Test O-piece (square) has only 1 rotation"""
        o_piece = PIECES[1]  # O-piece
        self.assertEqual(len(o_piece), 1, "O-piece should have 1 rotation")
        
        # Test square shape
        rotation = o_piece[0]
        self.assertIn('.##..', rotation[2])
        self.assertIn('.##..', rotation[3])
    
    def test_l_piece_rotations(self):
        """Test L-piece has 4 rotations and correct shape"""
        l_piece = PIECES[2]  # L-piece
        self.assertEqual(len(l_piece), 4, "L-piece should have 4 rotations")
        
        # Test first rotation (vertical L)
        first_rotation = l_piece[0]
        self.assertIn('..#..', first_rotation[1])
        self.assertIn('..#..', first_rotation[2])
        self.assertIn('..##.', first_rotation[3])
    
    def test_i_piece_rotations(self):
        """Test I-piece has 2 rotations and correct shape"""
        i_piece = PIECES[3]  # I-piece
        self.assertEqual(len(i_piece), 2, "I-piece should have 2 rotations")
        
        # Test horizontal line
        horizontal = i_piece[0]
        self.assertIn('####.', horizontal[2])
        
        # Test vertical line
        vertical = i_piece[1]
        block_count = sum(row.count('#') for row in vertical)
        self.assertEqual(block_count, 4, "I-piece should have 4 blocks")
    
    def test_j_piece_rotations(self):
        """Test J-piece has 4 rotations and is different from L-piece"""
        j_piece = PIECES[6]  # J-piece
        l_piece = PIECES[2]  # L-piece
        
        self.assertEqual(len(j_piece), 4, "J-piece should have 4 rotations")
        self.assertNotEqual(j_piece, l_piece, "J-piece should be different from L-piece")
        
        # Test first rotation (vertical J - mirror of L)
        first_rotation = j_piece[0]
        self.assertIn('.#...', first_rotation[1])
        self.assertIn('.#...', first_rotation[2])
        self.assertIn('.##..', first_rotation[3])

class TestTetrisGameLogic(unittest.TestCase):
    """Test Tetris game logic"""
    
    def setUp(self):
        self.game = Tetris()
    
    def test_initial_state(self):
        """Test game initial state"""
        self.assertEqual(len(self.game.grid), GRID_HEIGHT)
        self.assertEqual(len(self.game.grid[0]), GRID_WIDTH)
        self.assertEqual(self.game.piece_x, 3)
        self.assertEqual(self.game.piece_y, 0)
        self.assertIsNotNone(self.game.current_piece)
    
    def test_valid_move_empty_grid(self):
        """Test valid moves on empty grid"""
        # Should be able to move in empty space
        self.assertTrue(self.game.valid_move(self.game.current_piece, 0, 0))
        self.assertTrue(self.game.valid_move(self.game.current_piece, 5, 5))
    
    def test_invalid_move_boundaries(self):
        """Test invalid moves at boundaries"""
        # Create a piece that has blocks at the leftmost position
        left_edge_piece = [
            '#....',
            '#....',
            '#....',
            '#....',
            '.....'
        ]
        
        # Test left boundary with piece that has blocks on left edge
        self.assertFalse(self.game.valid_move(left_edge_piece, -1, 0))
        
        # Test right boundary - move far enough right that any piece will be invalid
        self.assertFalse(self.game.valid_move(self.game.current_piece, GRID_WIDTH, 0))
        
        # Test bottom boundary
        self.assertFalse(self.game.valid_move(self.game.current_piece, 0, GRID_HEIGHT))
    
    def test_move_left_right(self):
        """Test horizontal movement"""
        initial_x = self.game.piece_x
        
        # Move right
        self.game.move(1)
        self.assertEqual(self.game.piece_x, initial_x + 1)
        
        # Move left
        self.game.move(-1)
        self.assertEqual(self.game.piece_x, initial_x)
    
    def test_rotation(self):
        """Test piece rotation"""
        # Set to a piece that can rotate (T-piece)
        self.game.current_piece_type = 0  # T-piece
        self.game.current_rotation = 0
        self.game.current_piece = PIECES[0][0]
        
        initial_rotation = self.game.current_rotation
        self.game.rotate()
        
        # Should rotate to next state
        expected_rotation = (initial_rotation + 1) % len(PIECES[0])
        self.assertEqual(self.game.current_rotation, expected_rotation)
    
    def test_line_clearing(self):
        """Test line clearing functionality"""
        # Fill bottom row except one cell
        for x in range(GRID_WIDTH - 1):
            self.game.grid[GRID_HEIGHT - 1][x] = 1
        
        # Should not clear incomplete line
        initial_grid = [row[:] for row in self.game.grid]  # Deep copy
        self.game.clear_lines()
        self.assertEqual(self.game.grid[GRID_HEIGHT - 1][:-1], 
                        initial_grid[GRID_HEIGHT - 1][:-1])
        
        # Fill the last cell to complete the line
        self.game.grid[GRID_HEIGHT - 1][GRID_WIDTH - 1] = 1
        
        # Should clear complete line
        self.game.clear_lines()
        self.assertEqual(sum(self.game.grid[GRID_HEIGHT - 1]), 0, 
                        "Bottom row should be empty after clearing")
    
    def test_piece_placement(self):
        """Test piece placement on grid"""
        # Move piece to bottom
        while self.game.valid_move(self.game.current_piece, self.game.piece_x, self.game.piece_y + 1):
            self.game.piece_y += 1
        
        # Place the piece
        old_piece_type = self.game.current_piece_type
        self.game.place_piece()
        
        # Should have blocks on grid now
        has_blocks = any(any(row) for row in self.game.grid)
        self.assertTrue(has_blocks, "Grid should have blocks after placing piece")
        
        # Should have new piece
        self.assertIsNotNone(self.game.current_piece)

class TestTetrisPieceShapes(unittest.TestCase):
    """Test that each piece has the correct shape characteristics"""
    
    def count_blocks_in_piece(self, piece):
        """Helper to count blocks in a piece"""
        return sum(row.count('#') for row in piece)
    
    def test_all_pieces_have_4_blocks(self):
        """Test that all Tetris pieces have exactly 4 blocks"""
        piece_names = ['T', 'O', 'L', 'I', 'S', 'Z', 'J']
        
        for i, piece_rotations in enumerate(PIECES):
            for rotation_idx, rotation in enumerate(piece_rotations):
                block_count = self.count_blocks_in_piece(rotation)
                self.assertEqual(block_count, 4, 
                    f"{piece_names[i]}-piece rotation {rotation_idx} should have 4 blocks, got {block_count}")
    
    def test_piece_uniqueness(self):
        """Test that L and J pieces are actually different"""
        l_piece_first = PIECES[2][0]  # L-piece first rotation
        j_piece_first = PIECES[6][0]  # J-piece first rotation
        
        self.assertNotEqual(l_piece_first, j_piece_first, 
                           "L-piece and J-piece should be different")
    
    def test_s_z_piece_uniqueness(self):
        """Test that S and Z pieces are different"""
        s_piece_first = PIECES[4][0]  # S-piece first rotation
        z_piece_first = PIECES[5][0]  # Z-piece first rotation
        
        self.assertNotEqual(s_piece_first, z_piece_first, 
                           "S-piece and Z-piece should be different")

if __name__ == '__main__':
    # Run the tests
    unittest.main(verbosity=2)
