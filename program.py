from pacman import move_ghosts, play
from user_interface import key_input, print_map, show_msg_lost, show_msg_won

# creating our map for the game
# @ -> pacman
# G -> ghosts
# P -> pills
# . -> empty spaces
# | and - -> walls
map = [
    "|---------|", 
    "|G.P|...G.|", 
    "|..G..@...|", 
    "|.......|P|", 
    "|..|..G...|",
    "|P......P.|",
    "|---------|"
]

print("\nWelcome to the Pacman Game.\nUse your keyboard to play this.\nThe keys A (left), W (up), D (right) and S (down) controls the pacman.")

# This is the loop to play the game
game_finished = False
while not game_finished:
    print_map(map)
    key = key_input()
    valid_key, pacman_alive, won = play(map, key)
    
    pacman_was_hit = move_ghosts(map)

    if (not pacman_alive) or (pacman_was_hit):
        show_msg_lost()
        game_finished = True
    elif won:
        show_msg_won()
        game_finished = True