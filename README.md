# AWS Build Games Challenge - Maciej Bus

A professional Python pygame Tetris implementation for the [AWS Build Games Challenge](https://builder.aws.com/content/2y6egGcPAGQs8EwtQUM9KAONojz/build-games-challenge-build-classics-with-amazon-q-developer-cli).

## 🌟 **Version 0.2.1 - Professional Repository Organization**

This release introduces professional repository organization with industry-standard structure, SRS-compliant piece rotations, and comprehensive development infrastructure for scalable team collaboration.

## About the Challenge

This project is part of the AWS Build Games Challenge, where developers build classic games using Amazon Q Developer CLI assistance. The challenge focuses on recreating timeless games while leveraging AI-powered development tools.

## 🎮 **Game Features**

### **Core Gameplay:**
- Complete Tetris implementation with all 7 standard pieces (T, O, L, I, S, Z, J)
- Authentic NES Tetris colors and 3D block effects
- SRS-compliant piece rotations (Super Rotation System)
- Line clearing mechanics with authentic scoring
- Collision detection and boundary checking
- Smooth 60 FPS gameplay with keyboard controls

### **🏗️ Professional UI Architecture (v0.2.0):**
- **GameField Component**: Clean game area with contained grid lines (300×600px)
- **ScoreBoard Component**: Professional scoring and statistics display
- **HowToPlayPanel Component**: Always-visible player guidance
- **GameUI Coordinator**: Centralized component management
- **Visual Excellence**: Grid lines only in game field, no window-wide clutter

### **Enhanced User Experience:**
- Crystal-clear visual hierarchy with component boundaries
- Professional styling with subtle backgrounds
- Focused gameplay area without distractions
- Commercial-quality game presentation
- Intuitive information layout and enhanced readability

## 🚀 **Quick Start**

### **Run the Game:**
```bash
# Simple execution
python3 main.py

# Or use the launcher script
./scripts/run_tetris.sh
```

### **Run Tests:**
```bash
# Run all tests
python3 run_tests.py

# Or run specific test file
python3 -m pytest tests/
```

## Controls

- **Left/Right arrows**: Move pieces horizontally
- **Down arrow**: Soft drop (faster fall + 1 point per cell)
- **Up arrow**: Rotate pieces
- **Spacebar**: Hard drop (instant drop + 2 points per cell)
- **Close window**: Quit game

## 📁 **Project Structure**

```
Aws-Build-Games-Challenge-Maciej-Bus/
├── src/                    # Core game source code
│   ├── main.py            # Main game logic
│   ├── ui_components.py   # Modular UI components
│   ├── pieces.py          # Tetris pieces and SRS rotations
│   └── config.py          # Game configuration
├── tests/                 # Unit tests
│   └── test_tetris.py     # Comprehensive test suite
├── scripts/               # Utility scripts
│   ├── run_tetris.sh      # Game launcher
│   └── setup_environment.sh # Environment setup
├── docs/                  # Documentation
│   ├── user-guide/        # User documentation
│   ├── technical/         # Technical documentation
│   └── release-notes/     # Release notes
├── assets/                # Game assets (future)
├── main.py               # Entry point
├── run_tests.py          # Test runner
└── requirements.txt      # Dependencies
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the game:
```bash
python3 main.py
```

3. Run tests:
```bash
python3 run_tests.py
```

## Requirements

- Python 3.7+
- pygame 2.5.2+

## Development

This project includes comprehensive unit tests covering:
- Piece shape validation and SRS compliance
- Game logic testing
- Movement and rotation mechanics
- Boundary checking
- Line clearing functionality
- UI component validation

## 📚 Documentation

Comprehensive project documentation is available in the [`docs/`](docs/) directory:

### **User Documentation:**
- **[Quick Start Guide](docs/user-guide/QUICK_START.md)** - How to run and play the game

### **Technical Documentation:**
- **[SRS Compliance](docs/technical/SRS_COMPLIANCE.md)** - Super Rotation System implementation
- **[Development Guide](docs/DEV_BRANCH_README.md)** - Development workflow and guidelines
- **[Code Review](docs/CODE_REVIEW.md)** - Technical analysis and quality assessment  
- **[Improvement Plan](docs/IMPROVEMENT_PLAN.md)** - Implementation roadmap and examples
- **[Review Summary](docs/REVIEW_SUMMARY.md)** - Executive summary of code quality

### **Release Documentation:**
- **[Release Notes v0.2.1](docs/release-notes/RELEASE_NOTES_v0.2.1.md)** - Latest release details
- **[Release Notes v0.2.0](docs/release-notes/RELEASE_NOTES_v0.2.0.md)** - Previous release details

## Repository Status

🌟 **Version 0.2.1 Released** - Professional repository organization with SRS-compliant rotations!
