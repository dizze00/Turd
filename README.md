# Turd

A Python-based turtle graphics drawing tool that allows you to create patterns using a simple command language. Draw dots, lines, and complex patterns with intuitive commands and dynamic color cycling.

## Features

- **Dot-based drawing**: Create patterns using dots with precise positioning
- **Multiple drawing modes**: Horizontal, vertical, and directional drawing
- **Dynamic color support**: Change colors individually or cycle through multiple colors
- **Color cycling**: Automatically cycle through multiple colors for each dot
- **Interactive mode**: Real-time pattern creation with immediate feedback
- **Position control**: Precise control over turtle positioning and movement
- **HTTP API**: REST API for programmatic control (optional)

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
| `_` | Single color change | `_red....` changes color to red |
| `__` | Color cycling | `__red_blue_green__` cycles through colors |

### Special Commands

| Command | Description |
|---------|-------------|
| `quit` | Exit the program |
| `clear` | Clear the screen and reset position |
| `offset` | Change turtle position |
| `help` | Show available commands |
| `heading` | Display current turtle heading |
| `rs_rot` | Reset rotation to 180 degrees |

### Color Support

#### Single Color Change
Use the `_` command followed by a color name to change colors:

```
_red....     # Draw 4 red dots
_blue....    # Draw 4 blue dots
_white....   # Draw 4 white dots
```

#### Color Cycling (NEW!)
Use `__` to start and stop color cycling through multiple colors:

```
__red_violet_green_blue__....  # Draw 4 dots cycling through colors
```

**How color cycling works:**
1. Start with `__color1_color2_color3__`
2. Each dot automatically gets the next color in sequence
3. When reaching the last color, it cycles back to the first
4. Type `__` again to stop cycling and return to white

**Example:**
```
__red_blue_green__+,,.-f.+,,.../.+,,./...-,,./.-,,...-f.-,,.-f__
```
This creates a complex pattern with dots cycling through red, blue, and green colors.

Supported colors include: `red`, `blue`, `green`, `yellow`, `white`, `black`, `purple`, `orange`, `pink`, `brown`, `gray`, `cyan`, `magenta`, `violet`, etc.

## Examples

### Basic Patterns

```
...          # Three horizontal dots
.,.,.        # Three dots on separate lines
+,,.....     # Five dots going up
-,,.....     # Five dots going down
```

### Color Patterns

```
_red...._blue...._green....     # Individual color changes
__red_blue_green__....          # Color cycling
__red_violet_green_blue__....   # Four-color cycling
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

### Advanced Color Cycling Examples

```
# Rainbow pattern
__red_orange_yellow_green_blue_violet__........

# Simple cycling
__red_blue__+,,....-,,....

# Complex pattern with color cycling
__red_violet_green_blue__+,,.-f.+,,.../.+,,./...-,,./.-,,...-f.-,,.-f__
```

## Technical Details

### Variables

- `dot_size = 2`: Size of the drawing pen
- `turtle_scale = 0.2`: Size of the turtle cursor
- `dot_spacing = 8`: Spacing between dots (dot_size * 4)

### Color Cycling Variables

- `color_cycle = []`: List of colors to cycle through
- `color_cycle_index = 0`: Current position in color cycle
- `color_cycling = False`: Whether color cycling is active

### Drawing Logic

1. **Pattern Processing**: Input is processed through `process_dots()` function
2. **Color Cycling**: Special handling for `__` color cycling syntax
3. **Line-by-line Drawing**: Each line is drawn separately
4. **Mode Management**: Tracks vertical/horizontal drawing modes
5. **Position Control**: Precise positioning using turtle graphics commands

### HTTP API (Optional)

The program includes an HTTP server for programmatic control:

```bash
# Draw a pattern
curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"pattern": "..."}'

# Move turtle
curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"offset": [100, 50]}'

# Clear screen
curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"clear": true}'
```

## File Structure

```
Turt Dots/
├── turt.py      # Main program file
└── README.md    # This documentation
```

## Tips

1. **Start Simple**: Begin with basic patterns like `...` to understand the system
2. **Experiment with Colors**: Try color cycling for beautiful patterns
3. **Use Debug Info**: Pay attention to debug output to understand what's happening
4. **Clear Often**: Use `clear` command to start fresh when experimenting
5. **Position Control**: Use `offset` command to move to different areas of the screen
6. **Color Cycling**: Use `__` for automatic color changes - great for gradients and patterns

## Troubleshooting

- **Empty Input Error**: Just press Enter for default position (0,0)
- **Pattern Not Drawing**: Check debug output for mode and position information
- **Unexpected Movement**: Use `heading` command to check turtle direction
- **Color Issues**: Use `help` to see available color commands
- **Color Cycling Not Working**: Make sure to close with `__` and use valid color names

## Contributing

Feel free to modify and extend the program. Some ideas for improvements:
- Add more drawing commands
- Implement pattern saving/loading
- Add animation features
- Create a GUI interface
- Add more color options
- Implement pattern templates
- Add export to image functionality

## License

This project is open source and available for educational and personal use.
