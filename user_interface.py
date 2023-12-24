# creating interfaces for our game
ui_wall = [
    "......",
    "......",
    "......",
    "......"
]

ui_ghost = [
    " .-.  ",
    "| OO| ",
    "|   | ",
    "'^^^' "
]

ui_pacman = [
    " .--. ",
    "/ _.-'",
    "\\  '-.",
    " '--' "
]

ui_empty = [
    "      ",
    "      ",
    "      ",
    "      "
]

ui_pill = [
    "      ",
    " .-.  ",
    " '-'  ",
    "      "
]

# creating the fuction that will show the map for the user
def print_map(map):
    for row in map:
        for piece in range(4):
            for column in row:
                if (column == '|') or (column == '-'):
                    print(ui_wall[piece], end='')
                if column == 'G':
                    print(ui_ghost[piece], end='')
                if column == '@':
                    print(ui_pacman[piece], end='')
                if column == '.':
                    print(ui_empty[piece], end='')
                if column == 'P':
                    print(ui_pill[piece], end='')
                
            print("")
        
# creating a function to read what the user types
def key_input():
    return input()

# creating messages that will show for the user
def show_msg_lost():
    print("Pacman died, you lost the game!")
    
def show_msg_won():
    print("Congratulations! You won the game!")