import turtle as t

# Configuration
dot_size = 2
turtle_scale = 0.2
dot_spacing = dot_size * (dot_size * 2)

alphabet = "abcdefghijklmnopqrstuvwxyz"
color_offset = 0

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
                    t.dot()
                    t.penup()
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
            elif char == "_":
                color_offset = 0
                color_name = ""
                while i + 2 + color_offset < len(line) and line[i + 1 + color_offset].isalpha():
                    color_name += line[i + 1 + color_offset]
                    color_offset += 1
                for letter in color_name:
                    if letter == "V":
                        color_offset -= 1
                        color_name = color_name.replace(letter, "")
                if color_name != "":
                    try:
                        t.color(color_name)
                    except:
                        t.color("white")
                else:
                    t.color("white")
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

# Main loop
print("\n=== Turtle Drawing Mode ===\nEnter patterns to draw (type 'quit' to exit, 'clear' to clear screen, 'offset' to change position)\nDrawing Commands:\n  . = dot                    , = new line\n  ,, = vertical mode         +,, = vertical up mode\n  -,, = vertical down mode   / = backward movement\n  ' = start at x position    - = dash (move without drawing)\n  -- = double dash           /- = skip dot backward\n  _ = color change (e.g., _red)\nSpecial Commands: help, clear, offset, heading, quit")

running = True

while running:
    user_input = input("\nEnter pattern: ")

    if user_input.lower() == 'quit':
        running = False
    elif user_input.lower() == 'help':
        print("\n=== Turt-Dots Command Reference ===\nDrawing Commands:\n  . = dot                    , = new line\n  ,, = vertical mode         +,, = vertical up mode\n  -,, = vertical down mode   / = backward movement\n  ' = start at x position    - = dash (move without drawing)\n  -- = double dash           /- = skip dot backward\n  _ = color change (e.g., _red)\n\nSpecial Commands:\n  help    = show this help\n  clear   = clear screen and reset position\n  offset  = change turtle position\n  heading = show current turtle heading\n  quit    = exit program\n\nExamples:\n  ...          = three horizontal dots\n  +,,.....     = five dots going up\n  _red....     = four red dots\n  ...+,,......--......-,,...../.... = complex pattern")
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
    elif user_input.strip() == '':
        continue

    draw_pattern(user_input)

t.done()
