import random
import time
import pygame as py

DEAD = 0
LIVE = 1
SCR_DIM = SCR_WIDTH, SCR_HEIGHT = 900, 900
FRAMERATE = 15
DEAD_COLOR = py.Color("black")
LIVE_COLOR = py.Color("white")


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
                print('*', end=' ')
            else:
                print(' ', end=' ')

    # New line
    print('')

    # Another partition line below the board
    for x in range(state_width(state) * 2):
        print('-', end='')

    # New line
    print('')


# Render the game state using Pygame
def game_render(state):
    cell_num = state_width(state), state_height(state)
    cell_dim = cell_width, cell_height = (SCR_WIDTH // cell_num[0]), (SCR_HEIGHT // cell_num[1])

    for y in range(0, state_height(state)):
        for x in range(0, state_width(state)):
            if state[y][x]:
                py.draw.rect(screen, LIVE_COLOR, py.Rect((x * cell_width, y * cell_height), cell_dim))
            else:
                py.draw.rect(screen, DEAD_COLOR, py.Rect((x * cell_width, y * cell_height), cell_dim))

    py.display.flip()


def game_loop(init_state):
    next_state = init_state
    while True:
        e = py.event.poll()
        if e.type == py.QUIT:
            break

        clock.tick(FRAMERATE)

        game_render(next_state)
        next_state = next_board_state(next_state)

    py.quit()


if __name__ == "__main__":
    py.init()

    screen = py.display.set_mode(SCR_DIM)
    screen.fill(DEAD_COLOR)

    # set game clock speed based on framerate
    clock = py.time.Clock()

    init_state = random_state(100, 100)
    game_loop(init_state)

    # p = open("patterns\glider.rle", "r")

