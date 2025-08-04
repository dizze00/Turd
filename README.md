# Turt-Dots

A Python-based turtle graphics drawing tool that allows you to create patterns using a simple command language. Draw dots, lines, and complex patterns with intuitive commands.

## Features

- **Dot-based drawing**: Create patterns using dots with precise positioning
- **Multiple drawing modes**: Horizontal, vertical, and directional drawing
- **Color support**: Change colors dynamically during drawing
- **Interactive mode**: Real-time pattern creation with immediate feedback
- **Debug information**: Detailed logging for understanding drawing behavior
- **Position control**: Precise control over turtle positioning and movement

## Requirements

- Python 3.x
- Turtle graphics module (built-in with Python)

## Installation

1. Clone or download the project
2. Navigate to the project directory
3. Run the main script:
   ```bash
   python turt.py
   ```

## Usage

### Starting the Program

When you run `turt.py`, you'll be prompted to set the initial turtle position:

```
Turtle Start Offset X/Y (To the right and down. Set a , between x and y): 
```

Enter coordinates like `150,150` or just press Enter for `0,0`.

### Drawing Commands

| Command | Description | Example |
|---------|-------------|---------|
| `.` | Draw a dot at current position | `...` draws 3 dots |
| `,` | New line (move up) | `.,.,.` draws dots on separate lines |
| `,,` | Enter vertical mode | `+,,....` draws vertical line up |
| `+,,` | Vertical up mode | `+,,.....` draws 5 dots upward |
| `-,,` | Vertical down mode | `-,,.....` draws 5 dots downward |
| `/` | Backward movement | `/....` moves back then draws 4 dots |
| `'` | Start at x position | `'....` starts at beginning of line |
| `-` | Dash (move without drawing) | `-....` moves then draws |
| `--` | Double dash (draw dot and move) | `--....` draws dot, moves, then draws |
| `/-` | Skip dot backward | `/-....` skips one position back |
| `_` | Color change | `_red....` changes color to red |

### Special Commands

| Command | Description |
|---------|-------------|
| `quit` | Exit the program |
| `clear` | Clear the screen and reset position |
| `offset` | Change turtle position |
| `help` | Show available commands |
| `heading` | Display current turtle heading |

### Color Support

Use the `_` command followed by a color name to change colors:

```
_red....     # Draw 4 red dots
_blue....    # Draw 4 blue dots
_white....   # Draw 4 white dots
```

Supported colors include: `red`, `blue`, `green`, `yellow`, `white`, `black`, `purple`, `orange`, `pink`, `brown`, `gray`, `cyan`, `magenta`, etc.

## Examples

### Basic Patterns

```
...          # Three horizontal dots
.,.,.        # Three dots on separate lines
+,,.....     # Five dots going up
-,,.....     # Five dots going down
```

### Complex Patterns

```
...+,,......--......-,,...../.... 
```

This pattern creates:
1. Three horizontal dots
2. Five vertical dots going up
3. Six horizontal dots
4. Five vertical dots going down
5. Four horizontal dots after backward movement

### Color Patterns

```
_red...._blue...._green....
```

Creates a pattern with different colored dots.

## Technical Details

### Variables

- `pen_size = 2`: Size of the drawing pen
- `turtle_size = 0.2`: Size of the turtle cursor
- `t_f_one_dot = 8`: Spacing between dots (pen_size * 4)

### Drawing Logic

1. **Pattern Processing**: Input is processed through `make_dots()` function
2. **Line-by-line Drawing**: Each line is drawn separately
3. **Mode Management**: Tracks vertical/horizontal drawing modes
4. **Position Control**: Precise positioning using turtle graphics commands

### Debug Information

The program provides detailed debug output including:
- Input processing steps
- Drawing positions and movements
- Mode changes
- Color changes
- Position updates

## File Structure

```
Turt Dots/
├── turt.py      # Main program file
└── README.md    # This documentation
```

## Tips

1. **Start Simple**: Begin with basic patterns like `...` to understand the system
2. **Use Debug Info**: Pay attention to debug output to understand what's happening
3. **Experiment**: Try different combinations of commands to create unique patterns
4. **Clear Often**: Use `clear` command to start fresh when experimenting
5. **Position Control**: Use `offset` command to move to different areas of the screen

## Troubleshooting

- **Empty Input Error**: Just press Enter for default position (0,0)
- **Pattern Not Drawing**: Check debug output for mode and position information
- **Unexpected Movement**: Use `heading` command to check turtle direction
- **Color Issues**: Use `help` to see available color commands

## Contributing

Feel free to modify and extend the program. Some ideas for improvements:
- Add more drawing commands
- Implement pattern saving/loading
- Add animation features
- Create a GUI interface
- Add more color options

## License

This project is open source and available for educational and personal use.
