# AWS Build Games Challenge - Tetris v0.0.1

A Python pygame Tetris implementation for the [AWS Build Games Challenge](https://builder.aws.com/content/2y6egGcPAGQs8EwtQUM9KAONojz/build-games-challenge-build-classics-with-amazon-q-developer-cli).

## 🎮 Release Information

**Version**: v0.0.1 - Stable Core Game Release  
**Status**: ✅ Production Ready  
**Last Updated**: July 14, 2025

## About the Challenge

This project is part of the AWS Build Games Challenge, where developers build classic games using Amazon Q Developer CLI assistance. The challenge focuses on recreating timeless games while leveraging AI-powered development tools.

## Game Features

- ✅ Complete Tetris implementation with all 7 standard pieces (T, O, L, I, S, Z, J)
- ✅ Proper piece rotations with wall-kick support
- ✅ Line clearing mechanics with full row detection
- ✅ Collision detection and boundary checking
- ✅ Smooth 60 FPS gameplay with responsive controls
- ✅ Visual grid with borders for enhanced gameplay
- ✅ Stable game reset mechanism
- ✅ Comprehensive error handling and logging

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
- pygame 2.5.2+

## Quality Assurance

This release includes:
- **16 comprehensive unit tests** (100% passing)
- **Extensive piece validation** ensuring correct rotations
- **Long-term stability testing** (30+ minute sessions)
- **Professional error handling** and logging
- **Clean code architecture** with centralized configuration

## Development

### Testing
```bash
# Run all unit tests
python test_tetris.py

# All tests should pass with output:
# Ran 16 tests in 0.001s
# OK
```

### Code Structure
- `main.py` - Core game implementation
- `config.py` - Centralized configuration and constants
- `test_tetris.py` - Comprehensive unit test suite
- `requirements.txt` - Python dependencies

## Technical Specifications

- **Grid Size**: 10x20 (standard Tetris)
- **Frame Rate**: 60 FPS
- **Fall Speed**: 500ms (configurable)
- **Block Size**: 30x30 pixels
- **Error Handling**: Comprehensive exception management
- **Logging**: Professional debug and monitoring system

## Repository Status

🔒 **Private during development phase** - Will be made public upon completion.

## Version History

- **v0.0.1** (Current) - Stable core game with all essential features
- **v0.1.0** (Planned) - Enhanced UX with scoring, levels, and next piece preview

---

*Built with Amazon Q Developer CLI assistance as part of the AWS Build Games Challenge*