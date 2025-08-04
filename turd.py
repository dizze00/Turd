import turtle as t
from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Create HTTP server to receive commands
class TurtleAPIHandler(BaseHTTPRequestHandler):
    def do_POST(self):
         # Get the length of the request body
        content_length = int(self.headers['Content-Length'])
        # Read the request body
        post_data = self.rfile.read(content_length)
        # Parse JSON data
        command = json.loads(post_data.decode('utf-8'))
        
        # API Usage Examples:
        # To draw a pattern:
        # curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"pattern": "..."}'
        
        # To move turtle (x,y offset):
        # curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"offset": [100, 50]}'
        
        # To clear screen:
        # curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"clear": true}'

        # Process the command
        if 'pattern' in command:
            # Execute turtle pattern
            process_dots(command['pattern'])
        elif 'offset' in command:
            # Move turtle to new offset
            x, y = command['offset']
            t.teleport(t.pos()[0] + x, t.pos()[1] - y)
        elif 'clear' in command:
            # Clear screen
            t.clear()
            t.teleport(t.pos()[0], t.pos()[1])

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'ok'}).encode())

# Start HTTP server in a separate thread
def start_api_server():
    server = HTTPServer(('localhost', 8000), TurtleAPIHandler)
    print("API server started at http://localhost:8000")
    server.serve_forever()

# Start server in background thread
from threading import Thread
api_thread = Thread(target=start_api_server, daemon=True)
api_thread.start()

# Configuration
dot_size = 2
turtle_scale = 0.2
dot_spacing = dot_size * (dot_size * 2)

alphabet = "abcdefghijklmnopqrstuvwxyz"
color_offset = 0

# Color cycling variables
color_cycle = []
color_cycle_index = 0
color_cycling = False

t.turtlesize(turtle_scale)
t.pensize(dot_size)
t.color("white")
t.bgcolor("black")
t.speed(0)
t.setheading(180)

# Get initial offset
offset_input = input("Turtle Start Offset X/Y (To the right and down. Set a , between x and y): ")
if offset_input.strip() == "":
    offset_input = "0,0"
    
offset_parts = offset_input.split(",")
offset_x = int(offset_parts[0])
offset_y = int(offset_parts[1])
t.teleport(t.pos()[0] + offset_x, t.pos()[1] - offset_y)

def process_dots(input_str):
    result = ""
    i = 0
    while i < len(input_str):
        if input_str[i] == ",":
            if i + 1 < len(input_str) and input_str[i + 1] == "'":
                result += "\n'"
                i += 2
            elif i + 1 < len(input_str) and input_str[i + 1] == ",":
                result += "\nV"
                i += 2
            elif i + 1 < len(input_str) and input_str[i + 1] == "/":
                result += "\n\\"
                i += 2
            else:
                result += "\n"
                i += 1
        elif input_str[i] == "-":
            if i + 1 < len(input_str) and input_str[i + 1] == "-":
                result += "--"
                i += 2
            elif i + 2 < len(input_str) and input_str[i + 1] == "," and input_str[i + 2] == ",":
                result += "V-"
                i += 3
            else:
                result += "-"
                i += 1
        elif input_str[i] == "+":
            if i + 2 < len(input_str) and input_str[i + 1] == "," and input_str[i + 2] == ",":
                result += "V+"
                i += 3
            else:
                result += "+"
                i += 1
        elif input_str[i] == "(":
            if i + 3 < len(input_str) and input_str[i + 1] == "-" and input_str[i + 2] == "," and input_str[i + 3] == ",":
                result += "(V)"
                i += 4
            else:
                result += "("
                i += 1
        else:
            result += input_str[i]
            i += 1
    return result

def draw_pattern(pattern):
    global color_cycle, color_cycle_index, color_cycling
    processed_pattern = process_dots(pattern)
    lines = processed_pattern.splitlines()

    for line_num, line in enumerate(lines):
        if line_num > 0:
            t.penup()
            t.goto(t.pos()[0], t.pos()[1] + 2 * dot_spacing)
            t.pendown()
        
        vertical_mode = False
        vertical_direction = "down"
        i = 0
        
        while i < len(line):
            char = line[i]
            if char == "V":
                t.penup()
                t.backward(dot_spacing)
                t.setheading(180)

                if i + 1 < len(line) and line[i + 1] == "+":
                    vertical_mode = True
                    vertical_direction = "up"
                    t.setheading(90)
                    t.penup()
                    t.forward(dot_spacing)
                    t.pendown()
                    i += 2
                elif i + 1 < len(line) and line[i + 1] == "-":
                    vertical_mode = True
                    vertical_direction = "down"
                    t.setheading(270)
                    t.penup()
                    t.forward(dot_spacing)
                    t.pendown()
                    i += 2
                else:
                    vertical_mode = True
                    vertical_direction = "down"
                    t.setheading(270)
                    t.penup()
                    t.forward(dot_spacing)
                    t.pendown()
                    i += 1
                t.pendown()

            elif char == "-":
                if i + 1 < len(line) and (line[i + 1] == "f" or line[i + 1] == "F"):
                    vertical_mode = False
                    t.penup()
                    t.backward(dot_spacing)
                    t.setheading(180)
                    t.forward(dot_spacing)
                    t.pendown()
                    i += 2
                else:
                    vertical_mode = False
                    t.penup()
                    t.forward(dot_spacing)
                    t.pendown()
                    i += 1
            elif char == ".":
                # Apply color cycling if active
                if color_cycling and color_cycle:
                    try:
                        t.color(color_cycle[color_cycle_index])
                        color_cycle_index = (color_cycle_index + 1) % len(color_cycle)
                    except:
                        t.color("white")
                
                if vertical_mode:
                    t.dot()
                    t.penup()
                    t.setheading(90 if vertical_direction == "up" else 270)
                    t.forward(dot_spacing)
                    t.pendown()
                else:
                    t.dot()
                    t.penup()
                    t.forward(dot_spacing)
                    t.pendown()
                i += 1
            elif char == "/-":
                t.penup()
                t.backward(dot_spacing)
                t.pendown()
                i += 3
            
            elif char == "_" and i + 1 < len(line) and line[i + 1] == "_":
                # Handle color cycling start/stop
                if not color_cycling:
                    # Start color cycling - collect colors
                    color_cycle = []
                    color_cycle_index = 0
                    i += 2  # Skip "__"
                    
                    # Collect color names until we hit pattern commands or end
                    color_names = []
                    # Check if there's a color name right after "__" (before first "_")
                    if i < len(line) and line[i].isalpha():
                        color_name = ""
                        while i < len(line) and line[i].isalpha():
                            color_name += line[i]
                            i += 1
                        if color_name:
                            color_names.append(color_name.lower())
                    
                    while i < len(line):
                        if line[i] in ['.', ',', '+', '-', '/', "'", '(', ')', 'V']:
                            break
                        elif line[i] == "_" and i + 1 < len(line) and line[i + 1] == "_":
                            i += 2  # Skip closing "__"
                            break
                        elif line[i] == "_":
                            # Start of a color name
                            i += 1  # Skip underscore
                            color_name = ""
                            while i < len(line) and line[i].isalpha():
                                color_name += line[i]
                                i += 1
                            if color_name:
                                color_names.append(color_name.lower())
                        else:
                            i += 1
                    
                    if color_names:
                        color_cycle = color_names
                        color_cycling = True
                        print(f"Color cycling started with: {', '.join(color_cycle)}")
                    else:
                        print("No colors specified for cycling")
                else:
                    # Stop color cycling
                    color_cycling = False
                    color_cycle = []
                    color_cycle_index = 0
                    print("Color cycling stopped")
                    i += 2  # Skip "__"
            elif char == "_":
                # Single underscore color change (existing functionality)
                color_offset = 0
                color_name = ""
                while i + 1 + color_offset < len(line) and line[i + 1 + color_offset].isalpha():
                    color_name += line[i + 1 + color_offset]
                    color_offset += 1
                for letter in color_name:
                    if letter == "V":
                        color_offset -= 1
                        color_name = color_name.replace(letter, "")
                if color_name != "":
                    try:
                        t.color(color_name.lower())
                    except:
                        t.color("white")
                else:
                    t.color("white")
                if color_name != "":
                    print("Set color to:", color_name.capitalize())
                else:
                    print("Set color to:", "White")
                i += color_offset + 1
            elif char == "/":
                t.penup()
                t.backward(dot_spacing)
                t.pendown()
                vertical_mode = False
                t.penup()
                t.setheading(0)
                t.forward(dot_spacing)
                t.pendown()
                i += 1
            elif char == "'":
                vertical_mode = False
                t.penup()
                t.goto(t.pos()[0] - (i * dot_spacing), t.pos()[1])
                t.pendown()
                i += 1
            elif char in ["(", ")"]:
                i += 1
            else:
                i += 1

def main_loop():
    global color_cycling, color_cycle, color_cycle_index, dot_size, dot_spacing, turtle_scale
    
    print("\n=== Turtle Drawing Mode ===\nEnter patterns to draw (type 'quit' to exit, 'clear' to clear screen, 'offset' to change position)\nDrawing Commands:\n  . = dot                    , = new line\n  ,, = vertical mode         +,, = vertical up mode\n  -,, = vertical down mode   / = backward movement\n  ' = start at x position    - = dash (move without drawing)\n  -- = double dash           /- = skip dot backward\n  _ = color change (e.g., _red)\n  __ = color cycling (e.g., __red_blue_green__)\nSpecial Commands: help, clear, offset, heading, stop_cycling, ds, dsp, ts, quit")

    running = True

    while running:
        user_input = input("\nEnter pattern: ")

        if user_input.lower() == 'quit':
            running = False
        elif user_input.lower() == 'help':
            print("\n=== Turt-Dots Command Reference ===\nDrawing Commands:\n  . = dot                    , = new line\n  ,, = vertical mode         +,, = vertical up mode\n  -,, = vertical down mode   / = backward movement\n  ' = start at x position    - = dash (move without drawing)\n  -- = double dash           /- = skip dot backward\n  _ = color change (e.g., _red)\n  __ = color cycling (e.g., __red_blue_green__)\n\nSpecial Commands:\n  help         = show this help\n  clear        = clear screen and reset position\n  offset       = change turtle position\n  heading      = show current turtle heading\n  stop_cycling = stop color cycling\n  ds           = change dot size\n  dsp          = change dot spacing\n  ts           = change turtle scale\n  quit         = exit program\n\nExamples:\n  ...          = three horizontal dots\n  +,,.....     = five dots going up\n  _red....     = four red dots\n  __red_blue_green__.... = four dots cycling through colors\n  ...+,,......--......-,,...../.... = complex pattern")
            continue
        elif user_input.lower() == 'clear':
            t.clear()
            t.color("white")
            t.teleport(0, 0)
            t.setheading(180)
            continue
        elif user_input.lower() == 'offset':
            new_offset = input("New offset X/Y (comma separated): ").split(",")
            if len(new_offset) == 2:
                try:
                    new_x = int(new_offset[0])
                    new_y = int(new_offset[1])
                    t.penup()
                    t.goto(new_x, -new_y)
                    t.pendown()
                except ValueError:
                    print("Invalid offset values, please use numbers")
            else:
                print("Invalid offset format, use 'x,y'")
            continue
        elif user_input.lower() == 'heading':
            print(f"Current heading: {t.heading()}")
            continue
        elif user_input.lower() == 'rs_rot':
            t.setheading(180)
            continue
        elif user_input.lower() == 'stop_cycling':
            color_cycling = False
            color_cycle = []
            color_cycle_index = 0
            print("Color cycling stopped")
            continue
        elif user_input.lower() == 'ds':
            try:
                new_size = int(input("New dot size: (1 Default)\n"))
                dot_size = new_size * 2
                dot_spacing = dot_size * (dot_size / 2)
                t.pensize(dot_size)
                print(f"Dot size set to: {new_size}")
            except ValueError:
                print("Invalid input, using default size")
            continue
        elif user_input.lower() == 'rs_ds':
            dot_size = 2
            dot_spacing = dot_size * (dot_size * 2)
            t.pensize(dot_size)
            print("Dot size reset to: 1")
            continue
        elif user_input.lower() == 'rs_dsp':
            dot_spacing = dot_size * (dot_size * 2)
            print(f"Dot spacing reset to: {dot_spacing}")
            continue
        elif user_input.lower() == 'dsp':
            try:
                new_spacing = int(input("New dot spacing: \n"))
                dot_spacing = new_spacing
                print(f"Dot spacing set to: {dot_spacing}")
            except ValueError:
                print("Invalid input, keeping current spacing")
            continue
        elif user_input.lower() == 'ts':
            try:
                new_scale = float(input("New turtle scale: \n"))
                turtle_scale = new_scale
                t.turtlesize(turtle_scale)
                print(f"Turtle scale set to: {turtle_scale}")
            except ValueError:
                print("Invalid input, keeping current scale")
            continue
        elif user_input.strip() == '':
            continue

        draw_pattern(user_input)

# Start the main loop
main_loop()
t.done()
