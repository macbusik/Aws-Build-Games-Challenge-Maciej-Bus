# 🎮 Tetris - Quick Start Guide

## 🚀 **How to Run the Game**

### **Method 1: Direct Python Command**
```bash
cd /Users/macio/GitHub-projects/Aws-Build-Games-Challenge-Maciej-Bus
python3 main.py
```

### **Method 2: Convenient Launcher Script**
```bash
cd /Users/macio/GitHub-projects/Aws-Build-Games-Challenge-Maciej-Bus
./run_tetris.sh
```

### **Method 3: Setup Aliases (Recommended)**
```bash
# Run the setup script once
./setup_environment.sh

# Then restart your terminal or run:
source ~/.zshrc

# Now you can run from anywhere:
tetris
```

## 🎯 **Game Controls**

| Key | Action |
|-----|--------|
| `←` `→` | Move pieces left/right |
| `↑` | Rotate pieces |
| `↓` | Soft drop (+1 point per cell) |
| `SPACE` | Hard drop (+2 points per cell) |
| Close window | Quit game |

## 🧪 **Running Tests**

```bash
# Run all tests
python3 test_tetris.py

# Or with alias (after setup)
tetris-test
```

## 📋 **Requirements**

- **Python 3.7+** (you have 3.12.4 ✅)
- **pygame 2.5.2+** (you have 2.6.1 ✅)

## 🔧 **Troubleshooting**

### **If game doesn't start:**
1. Make sure you're in the correct directory
2. Check Python installation: `python3 --version`
3. Check pygame installation: `python3 -c "import pygame; print('OK')"`

### **If pygame is missing:**
```bash
pip3 install pygame
```

### **If you get permission errors:**
```bash
chmod +x run_tetris.sh
chmod +x setup_environment.sh
```

## 📁 **Project Structure**

```
Aws-Build-Games-Challenge-Maciej-Bus/
├── main.py              # Main game file
├── ui_components.py     # Modular UI components
├── pieces.py           # Tetris pieces and colors
├── config.py           # Game configuration
├── test_tetris.py      # Unit tests
├── run_tetris.sh       # Convenient launcher
├── setup_environment.sh # Environment setup
└── QUICK_START.md      # This guide
```

## 🎮 **Game Features**

- **Professional UI**: Modular component architecture
- **NES Tetris Colors**: Authentic piece colors and 3D effects
- **Complete Scoring**: Level progression and line clearing
- **Clean Grid**: Grid lines only in game field
- **Always-Visible Help**: Controls and scoring guide
- **60 FPS Gameplay**: Smooth, responsive controls

## 🏆 **Version Information**

- **Current Version**: v0.2.0
- **Architecture**: Modular UI components
- **Quality**: 37 unit tests passing
- **Performance**: 60 FPS stable gameplay

---

**🎯 Ready to play! Just run `python3 main.py` from the game directory.**
