import random
import pygame as py
from os import listdir

DEAD = 0
LIVE = 1
SCR_DIM = SCR_WIDTH, SCR_HEIGHT = 900, 900
FRAMERATE = 15
DEAD_COLOR = py.Color("black")
LIVE_COLOR = py.Color("white")


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        elif char != '!':
            if count == '':
                decode += char * 1
            else:
                decode += char * int(count)
            count = ''

    return decode


def load_pattern(pattern_name):

    # Reads pattern file line by line and omits newline character
    with open('patterns/' + pattern_name) as f:
        pattern_file = f.read().splitlines()

    # Iterates through each line, stores the header line and encoded data, skips over comments
    encoded_data = ''
    for line in pattern_file:
        if line[0] == '#':
            continue
        elif line[0] == 'x':
            header_line = line
        else:
            encoded_data += line

    # Get the x and y dimensions of the pattern from the header line
    header_line = header_line.split(',')
    dim = []
    for i in header_line[0:2]:
        x = ''
        for char in i:
            if char.isdigit():
                x += char

        dim.append(int(x))

    # Creates a blank pattern with proper dimensions
    pattern = [[DEAD] * dim[0] for i in range(dim[1])]

    # Split pattern by line and decode
    formatted_data = encoded_data.split('$')
    decoded_data = []
    for i in range(len(formatted_data)):
        decoded_data.append(rle_decode(formatted_data[i]))

    # Use data to create pattern
    # dim = [x, y]
    for y in range(dim[1]):
        for x in range(dim[0]):
            if y >= len(decoded_data):
                continue
            if x >= len(decoded_data[y]):
                continue
            if decoded_data[y][x] == 'o':
                pattern[y][x] = LIVE

    ascii_render(pattern)

    game_board = dead_state(100, 100)

    # Put pattern in center of game board
    # dim = [x, y]
    for y in range(dim[1]):
        for x in range(dim[0]):
            game_board[y + 20][x + 20] = pattern[y][x]

    return game_board



# Returns a board state with specified width and height where each cell is dead
def dead_state(w, h):
    return [[DEAD] * w for i in range(h)]


# Returns a board state of specified width and height where the state of each cell is randomly determined
def random_state(w, h):
    state = dead_state(w, h)
    for y in range(state_height(state)):
        for x in range(state_width(state)):
            random_number = random.random()
            if random_number > .6:
                state[y][x] = LIVE
            else:
                state[y][x] = DEAD
    return state


def state_width(state):
    return len(state[0])


def state_height(state):
    return len(state)


def next_cell_value(cell_coords, state):
    width = state_width(state)
    height = state_height(state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0

    # Iterate over all of the cell's neighbors
    for y1 in range((y - 1), (y + 2)):
        if y1 < 0 or y1 >= height: continue  # Skips neighbors out of range
        for x1 in range((x - 1), (x + 2)):
            if x1 < 0 or x1 >= width: continue  # Skips neighbors out of range
            if x1 == x and y1 == y: continue  # Skips cell count if it is the cell itself

            if state[y1][x1] == LIVE:
                n_live_neighbors += 1

    # determine cell value depending on the number of alive neighbors
    if state[y][x] == LIVE:
        if n_live_neighbors <= 1:
            return DEAD
        elif n_live_neighbors <= 3:
            return LIVE
        else:
            return DEAD
    else:
        if n_live_neighbors == 3:
            return LIVE
        else:
            return DEAD


def next_board_state(init_state):
    width = state_width(init_state)
    height = state_height(init_state)
    next_state = dead_state(width, height)

    for y in range(0, height):
        for x in range(0, width):
            next_state[y][x] = next_cell_value((x, y), init_state)

    return next_state


# Prints the state of a board to terminal in ascii form
def ascii_render(state):
    # Draws a partition line above the board
    for x in range(state_width(state) * 2):
        print('-', end='')

    # Traverses the board and renders it to terminal
    for y in range(state_height(state)):
        print('')
        for x in range(state_width(state)):
            if state[y][x] == LIVE:
                print('O', end=' ')
            else:
                print('.', end=' ')

    # New line
    print('')

    # Another partition line below the board
    for x in range(state_width(state) * 2):
        print('-', end='')

    # New line
    print('')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]
    return rgb


# Render the game state using Pygame
def game_render(state, screen):
    cell_num = state_width(state), state_height(state)
    cell_dim = cell_width, cell_height = (SCR_WIDTH // cell_num[0]), (SCR_HEIGHT // cell_num[1])

    for y in range(0, state_height(state)):
        for x in range(0, state_width(state)):
            if state[y][x]:
                rgb = random_color()
                py.draw.rect(screen, (rgb[0], rgb[1], rgb[2]), py.Rect((x * cell_width, y * cell_height), cell_dim))
            else:
                py.draw.rect(screen, DEAD_COLOR, py.Rect((x * cell_width, y * cell_height), cell_dim))

    py.display.flip()


def game_loop(init_state):
    py.init()
    clock = py.time.Clock()
    screen = py.display.set_mode(SCR_DIM)
    screen.fill(DEAD_COLOR)
    next_state = init_state
    while True:
        e = py.event.poll()
        if e.type == py.QUIT:
            break

        clock.tick(FRAMERATE)

        game_render(next_state, screen)
        next_state = next_board_state(next_state)

    py.quit()


if __name__ == "__main__":

    print("Welcome to the Game of Life!")
    print("Select an initial game state: ")
    print("[1] Start with a soup (randomized game state)")
    print("[2] Start with a pattern")

    choice = False
    while not choice:
        choice = input()
        print(choice)
        if choice != '1' and choice != '2':
            print("Please input a valid number: ")
            choice = False

        if choice == '1':
            game_loop(random_state(100, 100))
            choice == False
        elif choice == '2':
            break

    print("Please select a pattern to load:")
    patterns = listdir('patterns')

    choice = False
    while not choice:
        count = 0
        for file in patterns:
            count += 1
            print("[{}]".format(count), file)

        choice = input()

        try:
            val = int(choice)
            if (val - 1) not in range(len(patterns)):
                print("Please input a valid number: ")
                choice = False
            else:
                pattern_name = str(patterns[val-1])
                init_state = load_pattern(pattern_name)
                game_loop(init_state)
        except ValueError:
            print("Please input a valid number: ")
            choice = False

    # init_state = random_state(100, 100)
    # game_loop(init_state)

    #init_state = load_pattern("patterns/glider.rle")
    #game_loop(init_state)
    # load_pattern("patterns/gosperglidergun.rle")
    # load_pattern("patterns/figureeight.rle")
    # load_pattern("patterns/tannersp46.rle")
    # load_pattern("patterns/pentadecathalon.rle")









