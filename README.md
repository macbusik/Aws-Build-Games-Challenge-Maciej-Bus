# AWS Build Games Challenge - Maciej Bus

A Python pygame Tetris implementation for the [AWS Build Games Challenge](https://builder.aws.com/content/2y6egGcPAGQs8EwtQUM9KAONojz/build-games-challenge-build-classics-with-amazon-q-developer-cli).

## About the Challenge

This project is part of the AWS Build Games Challenge, where developers build classic games using Amazon Q Developer CLI assistance. The challenge focuses on recreating timeless games while leveraging AI-powered development tools.

## Game Features

- Complete Tetris implementation with all 7 standard pieces (T, O, L, I, S, Z, J)
- Proper piece rotations with wall-kick support
- Line clearing mechanics
- Collision detection and boundary checking
- Smooth gameplay with keyboard controls
- Visual grid with borders

## Controls

- **Left/Right arrows**: Move pieces horizontally
- **Down arrow**: Soft drop (faster fall)
- **Up arrow or Spacebar**: Rotate pieces
- **Close window**: Quit game

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the game:
```bash
python main.py
```

3. Run tests:
```bash
python test_tetris.py
```

## Requirements

- Python 3.7+
- pygame 2.5.2

## Development

This project includes comprehensive unit tests covering:
- Piece shape validation
- Game logic testing
- Movement and rotation mechanics
- Boundary checking
- Line clearing functionality

## Repository Status

🔒 **Private during development phase** - Will be made public upon completion.