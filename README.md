# AWS Build Games Challenge - Maciej Bus

A professional Python pygame Tetris implementation for the [AWS Build Games Challenge](https://builder.aws.com/content/2y6egGcPAGQs8EwtQUM9KAONojz/build-games-challenge-build-classics-with-amazon-q-developer-cli).

## 🌟 **Version 0.2.0 - Modular UI Architecture**

This release introduces a revolutionary modular UI architecture that transforms the game into a professional, commercial-quality experience with clean component separation and enhanced visual design.

## About the Challenge

This project is part of the AWS Build Games Challenge, where developers build classic games using Amazon Q Developer CLI assistance. The challenge focuses on recreating timeless games while leveraging AI-powered development tools.

## 🎮 **Game Features**

### **Core Gameplay:**
- Complete Tetris implementation with all 7 standard pieces (T, O, L, I, S, Z, J)
- Authentic NES Tetris colors and 3D block effects
- Proper piece rotations with wall-kick support
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

## Controls

- **Left/Right arrows**: Move pieces horizontally
- **Down arrow**: Soft drop (faster fall + 1 point per cell)
- **Up arrow**: Rotate pieces
- **Spacebar**: Hard drop (instant drop + 2 points per cell)
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

## 📚 Documentation

Comprehensive project documentation is available in the [`docs/`](docs/) directory:

- **[Development Guide](docs/DEV_BRANCH_README.md)** - Development workflow and guidelines
- **[Code Review](docs/CODE_REVIEW.md)** - Technical analysis and quality assessment  
- **[Improvement Plan](docs/IMPROVEMENT_PLAN.md)** - Implementation roadmap and examples
- **[Review Summary](docs/REVIEW_SUMMARY.md)** - Executive summary of code quality

Release notes are maintained in their respective release branches.

## Repository Status

🌟 **Version 0.2.0 Released** - Professional modular UI architecture with component-based design!
