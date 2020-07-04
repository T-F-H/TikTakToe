import keyboard

# Validating integern entry for level_height, width
def inputInt(message):
    while True:
        try:
            userInput = int(input(message))       
        except ValueError:
            print("Please only enter Integers!")
            continue
        else:
            return userInput 
            break 

pos = 1     # Position in the level (1 always top-left like phone)
level_height = inputInt("Level Height: ")
level_width = inputInt("Level Width: ")
x_turn = True   # if it's x's turn
xs = [] # Tuple of squares that x has
os = [] # Tuple of squares that o has

def print_level():
    draw_pos = 1 # The cell currently being drawn
    # Each cell is 3x3 with a border
    
    # Absolute top row
    level = "\n"*100 + "#"
    for x in range(level_width):
        level += "####"
    
    for y in range(level_height): # Every row in level
        # upper of row
        level += "\n#"
        for x in range(level_width):
            level += "   #"
        
        # middle of each row
        level += "\n#"
        for x in range(level_width):
            owner = " " # Who owns the square
            if draw_pos in xs:
                owner = "X"
            elif draw_pos in os:
                owner = "O"
            if draw_pos == pos:
                level += ">"+owner+"<#"
            else:
                level += " "+owner+" #"
            draw_pos += 1

        # lower of row
        level += "\n#"
        for x in range(level_width):
            level += "   #"
        
        # bottom of row
        level += "\n#"
        for x in range(level_width):
            level += "####"
    print(level)
    global x_turn
    if x_turn:
        print("It is Player X's turn.")
    else:
        print("It is Player O's turn.")

def right():
    global pos, level_width
    if pos % level_width != 0: # If not at right edge 
        pos += 1
    print_level()

def left():
    global pos, level_width
    if pos % level_width != 1: # If not at left edge 
        pos -= 1
    print_level()

def up():
    global pos, level_width, level_height
    if pos > level_width: # If not at top edge 
        pos -= level_width
    print_level()

def down():
    global pos, level_width, level_height
    if pos <= level_width*level_height - level_width: # If not at botton edge 
        pos += level_width
    print_level()

def place():
    global pos, xs, os, x_turn
    if x_turn:
        if not pos in os:
            xs.append(pos)
            x_turn = not x_turn
    else:
        if not pos in xs:
            os.append(pos)
            x_turn = not x_turn
    print_level()

print_level()

keyboard.add_hotkey('space', place)
keyboard.add_hotkey('d', right)
keyboard.add_hotkey('a', left)
keyboard.add_hotkey('w', up)
keyboard.add_hotkey('s', down)
keyboard.add_hotkey('right', right)

keyboard.add_hotkey('left', left)
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)

keyboard.wait()
