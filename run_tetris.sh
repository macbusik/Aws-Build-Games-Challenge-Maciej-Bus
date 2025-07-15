#!/bin/bash
# Tetris Game Launcher Script
# AWS Build Games Challenge - Maciej Bus

echo "🎮 Starting Tetris Game..."
echo "📍 Location: $(pwd)"
echo "🐍 Python: $(python3 --version)"
echo "🎨 Pygame: $(python3 -c 'import pygame; print(f"v{pygame.version.ver}")' 2>/dev/null)"
echo ""

# Check if we're in the right directory
if [ ! -f "main.py" ]; then
    echo "❌ Error: main.py not found in current directory"
    echo "Please run this script from the Tetris game directory"
    exit 1
fi

# Check if pygame is installed
if ! python3 -c "import pygame" 2>/dev/null; then
    echo "❌ Error: pygame not installed"
    echo "Please install pygame: pip3 install pygame"
    exit 1
fi

echo "🚀 Launching Tetris..."
echo "   Controls: Arrow keys + Spacebar for hard drop"
echo "   Close window to quit"
echo ""

# Run the game
python3 main.py

echo ""
echo "🎮 Thanks for playing Tetris!"
