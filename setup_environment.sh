#!/bin/bash
# Environment Setup for Tetris Game
# This script helps configure your terminal for easy game running

echo "🔧 Setting up Tetris Game Environment..."

# Check current shell
if [[ "$SHELL" == *"zsh"* ]]; then
    SHELL_CONFIG="$HOME/.zshrc"
    echo "📝 Detected zsh shell, using $SHELL_CONFIG"
elif [[ "$SHELL" == *"bash"* ]]; then
    SHELL_CONFIG="$HOME/.bashrc"
    echo "📝 Detected bash shell, using $SHELL_CONFIG"
else
    echo "⚠️  Unknown shell: $SHELL"
    SHELL_CONFIG="$HOME/.profile"
fi

# Get current directory
TETRIS_DIR="$(pwd)"

echo "📍 Tetris game directory: $TETRIS_DIR"

# Create alias for easy game running
echo ""
echo "🎯 Creating convenient aliases..."

# Check if python3 works
if command -v python3 &> /dev/null; then
    echo "✅ python3 found at: $(which python3)"
    
    # Create temporary alias file
    cat > /tmp/tetris_aliases.sh << EOF
# Tetris Game Aliases - Added by setup script
alias tetris='cd "$TETRIS_DIR" && python3 main.py'
alias tetris-test='cd "$TETRIS_DIR" && python3 test_tetris.py'
alias tetris-dir='cd "$TETRIS_DIR"'

# Python alias for convenience (if python command doesn't exist)
if ! command -v python &> /dev/null; then
    alias python='python3'
fi
EOF

    echo "📋 Suggested aliases to add to your $SHELL_CONFIG:"
    echo ""
    cat /tmp/tetris_aliases.sh
    echo ""
    
    read -p "🤔 Would you like to add these aliases to your shell config? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "" >> "$SHELL_CONFIG"
        echo "# Tetris Game Aliases - Added $(date)" >> "$SHELL_CONFIG"
        cat /tmp/tetris_aliases.sh >> "$SHELL_CONFIG"
        echo "✅ Aliases added to $SHELL_CONFIG"
        echo "🔄 Please run: source $SHELL_CONFIG"
        echo "   Or restart your terminal to use the new aliases"
    else
        echo "⏭️  Skipped adding aliases to shell config"
        echo "💡 You can manually add them later if needed"
    fi
    
    rm /tmp/tetris_aliases.sh
else
    echo "❌ python3 not found! Please install Python 3"
    exit 1
fi

echo ""
echo "🎮 Setup complete! You can now run the game with:"
echo "   • python3 main.py (from this directory)"
echo "   • ./run_tetris.sh (convenient launcher)"
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "   • tetris (from anywhere, after reloading shell)"
fi
echo ""
echo "🧪 To run tests: python3 test_tetris.py"
echo "📁 Game directory: $TETRIS_DIR"
