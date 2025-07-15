#!/usr/bin/env python3
"""
Tetris Game - Main Entry Point
AWS Build Games Challenge - Maciej Bus

Professional Tetris implementation with:
- Modular UI architecture
- SRS-compliant piece rotations
- NES Tetris colors and scoring
- 60 FPS gameplay
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the game
if __name__ == "__main__":
    try:
        from main import main
        main()
    except ImportError as e:
        print(f"❌ Error importing game: {e}")
        print("Make sure you're running from the project root directory")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error running game: {e}")
        sys.exit(1)
