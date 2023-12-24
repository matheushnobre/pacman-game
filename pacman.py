import random

# creating a function to play the game
# this function returns three booleans
# the first indicates wheter the pressed key was a valid key
# the second indicates wheter the pacman is still alive
# the tird indicates wheter the pacman won the game
def play(map, key):
    next_x, next_y = next_position(map, key)
    
    # if is an invalid key
    is_an_invalid_key = next_x == -1 and next_y == -1
    if is_an_invalid_key:
        return False, True, False
    
    # if is not within borders
    if not within_borders(map, next_x, next_y):
        return False, True, False
    
    # if it is a wall
    if is_a_wall(map, next_x, next_y):
        return False, True, False
    
    # if it is a ghost
    if is_a_ghost(map, next_x, next_y):
        return True, False, False

    # moving pacman
    move_pacman(map, next_x, next_y)
    
    # checking the remaining quantity of pills
    remaining_pills = total_pills(map)
    if remaining_pills == 0:
        return True, True, True
    else:
        return True, True, False

# creating a function to find the pacman position in the game
def find_pacman(map):
    pacman_x = -1 # initialize a value for the x pacman coordinate
    pacman_y = -1 # initialize a value for the y pacman coordinate
    
    # creating a loop to traverse the map
    for x in range(len(map)): 
        for y in range(len(map[x])):
            if map[x][y] == '@': # this condition represents that pacman was found
                pacman_x = x
                pacman_y = y
                break
    
    return pacman_x, pacman_y # this function return the pacman coordinates

# creating a function to move pacman
def move_pacman(map, next_pacman_x, next_pacman_y):
    pacman_x, pacman_y = find_pacman(map)
    
    # the place where the pacman was is now empty
    new_row = map[pacman_x][0:pacman_y] + '.' + map[pacman_x][pacman_y+1:] # everything to the left + '.' + everything to the right
    map[pacman_x] = new_row
    
    # the new place has the pacman
    new_row_2 = map[next_pacman_x][0:next_pacman_y] + '@' + map[next_pacman_x][next_pacman_y+1:] # everything to the left + '@' + everything to the right
    map[next_pacman_x] = new_row_2

# creating a function to calculate the pacman next position using the keyboard
def next_position(map, key):
    x, y = find_pacman(map)
    next_x = -1
    next_y = -1
    
    # a -> left
    if key == 'a':
        next_x = x
        next_y = y-1
    # w -> up
    elif key == 'w':
        next_x = x-1
        next_y = y
    # d -> right
    elif key == 'd':
        next_x = x
        next_y = y+1
    # a -> down
    elif key == 's':
        next_x = x+1
        next_y = y
    return next_x,next_y

# creating a function to verificate if it is not within borders
def within_borders(map, next_x, next_y):
    number_of_rows = len(map)
    x_is_valid = 0 <= next_x < number_of_rows
    
    number_of_columns = len(map[0])
    y_is_valid = 0 <= next_y < number_of_columns
    
    return x_is_valid and y_is_valid

# creating a function to verificate if a position is a wall
def is_a_wall(map, next_x, next_y):
    return (map[next_x][next_y] == '|') or (map[next_x][next_y] == '-')

# creating a function to verificate if a position is a ghost
def is_a_ghost(map, next_x, next_y):
    return map[next_x][next_y] == 'G'

# creating a function to verificate if a position is a pill
def is_a_pill(map, next_x, next_y):
    return (map[next_x][next_y] == '|') or (map[next_x][next_y] == 'P')

# creating a function to verificate if a position is a pacman
def is_a_pacman(map, next_x, next_y):
    return (map[next_x][next_y] == '|') or (map[next_x][next_y] == '@')

# creating a function to define the quantity of pills in the map
def total_pills(map):
    number_of_pills = 0
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'P':
                number_of_pills += 1
    return number_of_pills

# creating a function to find ghosts
def find_ghosts(map):
    all_ghosts = []
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 'G':
                all_ghosts.append([x, y])
    return all_ghosts
 
# creating a function to move ghosts
def move_ghosts(map):
    all_ghosts = find_ghosts(map)
    # loop to traverse all ghosts
    for ghost in all_ghosts:
        ghost_x = ghost[0]
        ghost_y = ghost[1]
        
        # this is the possible directions for the ghosts
        possible_directions = [
            [ghost_x, ghost_y - 1], # left
            [ghost_x, ghost_y + 1], # right
            [ghost_x - 1, ghost_y], # up
            [ghost_x + 1, ghost_y] # down
        ]
        
        # select a random possible movement and get the x, y of the movement
        random_number = random.randint(0, 3)
        next_ghost_x = possible_directions[random_number][0]
        next_ghost_y = possible_directions[random_number][1]
        
        # checks actually before move it
        if not within_borders(map, next_ghost_x, next_ghost_y):
            continue
        if is_a_wall(map, next_ghost_x, next_ghost_y):
            continue
        if is_a_ghost(map, next_ghost_x, next_ghost_y):
            continue
        if is_a_pill(map, next_ghost_x, next_ghost_y):
            continue
        if is_a_pacman(map, next_ghost_x, next_ghost_y):
            return True
        
        # moving the ghost to the random position
        new_row = map[ghost_x][0:ghost_y] + '.' + map[ghost_x][ghost_y+1:] # everything to the left + '.' + everything to the right
        map[ghost_x] = new_row
        new_row_2 = map[next_ghost_x][0:next_ghost_y] + 'G' + map[next_ghost_x][next_ghost_y+1:] # everything to the left + '@' + everything to the right
        map[next_ghost_x] = new_row_2
        
    return False