# AWS Build Games Challenge - Tetris v0.1.0 "Scored Game"

A Python pygame Tetris implementation with authentic NES scoring for the [AWS Build Games Challenge](https://builder.aws.com/content/2y6egGcPAGQs8EwtQUM9KAONojz/build-games-challenge-build-classics-with-amazon-q-developer-cli).

## 🎮 Release Information

**Version**: v0.1.0 "Scored Game" - Enhanced Gameplay Release  
**Status**: ✅ Production Ready with Scoring System  
**Last Updated**: July 14, 2025  
**Previous**: v0.0.1 (Core Game)

## 🏆 **New in v0.1.0: NES Tetris Scoring**

### **Authentic Scoring System**
- **Single Line**: 40 × (level + 1) points
- **Double Line**: 100 × (level + 1) points  
- **Triple Line**: 300 × (level + 1) points
- **Tetris (4 lines)**: 1200 × (level + 1) points
- **Soft Drop**: 1 point per cell manually dropped

### **Level Progression**
- **Dynamic Levels**: 0-29 with authentic NES speed curve
- **Progression**: Every 10 lines cleared advances one level
- **Speed Increase**: Game accelerates from 800ms to 17ms fall time
- **Visual Feedback**: Real-time level and speed display

### **Professional UI**
- **Score Display**: 8-digit format with leading zeros
- **Statistics Panel**: Score, Level, Lines, Pieces, Speed
- **Expanded Window**: 550px width for enhanced layout
- **Color-coded Info**: Professional typography and colors

## About the Challenge

This project is part of the AWS Build Games Challenge, where developers build classic games using Amazon Q Developer CLI assistance. The challenge focuses on recreating timeless games while leveraging AI-powered development tools.

## Game Features

### **Core Gameplay**
- ✅ Complete Tetris implementation with all 7 standard pieces (T, O, L, I, S, Z, J)
- ✅ Proper piece rotations with wall-kick support
- ✅ Line clearing mechanics with full row detection
- ✅ Collision detection and boundary checking
- ✅ Smooth 60 FPS gameplay with responsive controls

### **Scoring & Progression**
- ✅ **NES Tetris scoring system** with authentic point values
- ✅ **Dynamic level progression** (0-29) with speed increases
- ✅ **Multi-line clear bonuses** for strategic play
- ✅ **Soft drop scoring** for manual piece acceleration
- ✅ **Real-time statistics** display and tracking

### **Visual & UI**
- ✅ **Professional score panel** with comprehensive statistics
- ✅ **Visual grid** with borders for enhanced gameplay
- ✅ **Color-coded information** display
- ✅ **Level and speed indicators** for difficulty awareness

## Controls

- **Left/Right arrows**: Move pieces horizontally
- **Down arrow**: Soft drop (faster fall + 1 point per cell)
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
- pygame 2.5.2+

## Quality Assurance

This release includes:
- **23 comprehensive unit tests** (100% passing)
- **NES Tetris scoring validation** ensuring authentic gameplay
- **Extended stability testing** (8+ minute continuous sessions)
- **Professional error handling** and logging system
- **Score progression verification** (0 → 5,522+ points tested)

## Development

### Testing
```bash
# Run all unit tests (including 7 new scoring tests)
python test_tetris.py

# Expected output:
# Ran 23 tests in 0.015s
# OK
```

### Code Structure
- `main.py` - Core game implementation with scoring system
- `config.py` - Centralized configuration including scoring constants
- `test_tetris.py` - Comprehensive unit test suite (23 tests)
- `requirements.txt` - Python dependencies

## Technical Specifications

- **Grid Size**: 10x20 (standard Tetris)
- **Window Size**: 550x600 pixels (expanded for score display)
- **Frame Rate**: 60 FPS
- **Fall Speed**: Dynamic 800ms → 17ms (levels 0-29)
- **Scoring**: Authentic NES Tetris point system
- **Level Progression**: Every 10 lines cleared
- **Error Handling**: Comprehensive exception management
- **Logging**: Professional debug and scoring event system

## Gameplay Experience

### **What Players Get**
- **Authentic NES Tetris feel** with proper scoring and progression
- **Motivational gameplay** with score-driven improvement
- **Progressive challenge** maintaining engagement through levels
- **Strategic depth** with multi-line clearing optimization
- **Professional presentation** with clean UI and statistics

### **Score Progression Example**
```
Level 0: Single=40pts, Double=100pts, Triple=300pts, Tetris=1200pts
Level 1: Single=80pts, Double=200pts, Triple=600pts, Tetris=2400pts
Level 2: Single=120pts, Double=300pts, Triple=900pts, Tetris=3600pts
...and so on up to Level 29
```

## Repository Status

🔒 **Private during development phase** - Will be made public upon completion.

## Version History

- **v0.1.0** (Current) - Enhanced gameplay with NES Tetris scoring system
- **v0.0.1** - Stable core game with all essential features

## Branch Structure

- **`main`** - Deployment-ready source of truth
- **`dev`** - Active development branch  
- **`v0.1.0-scored-game`** - Current release branch
- **`v0.0.1`** - Previous stable release

---

*Built with Amazon Q Developer CLI assistance as part of the AWS Build Games Challenge*

**🎯 Ready for competitive play with authentic NES Tetris scoring!** 🏆
