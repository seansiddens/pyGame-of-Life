import random
import time

# Returns a board state with specified width and height where each cell is dead
def dead_state(w, h):
    a = [[0] * w for i in range(h)]
    return a

# Prints the state of a board to terminal in a nice format
def render(state):
    # Draws a partition line above the board
    for i in range(len(state[0]) * 2):
        print('-', end='')

    # Traverses the board, outputting a * for each alive cell, and a blank space for each dead cell. Properly formats so board is even and equally spaced.
    for i in range(len(state)):
        print('')
        for j in range(len(state[i])):
            if state[i][j] == 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')

    # New line
    print('')

    # Another partition line below the board
    for i in range(len(state[0]) * 2):
        print('-', end='')
    
    # New line
    print('')


# Returns a board state of specified width and height where the state of each cell is randomly determined
def random_state(w, h):
    state = dead_state(w, h)

    for i in range(len(state)):
        for j in range(len(state[i])):
            randomNumber = random.random()
            if randomNumber >= .8:
                state[i][j] = 1
            else:
                state[i][j] = 0
    return state

'''
def next_board_state(state):

    nextState = state.copy()
    for i in range(len(state)):
        for j in range(len(state[i])):
            
            # Counter to keep track of alive neighbors
            liveCount = 0
            
            # Checks if cell is already alive
            if state[i][j] == 1:
                aliveCheck = True
            else:
                aliveCheck = False

            # Center Cell 
            if i > 0 and i < (len(state) - 1) and j > 0 and j < (len(state[i]) - 1):
                for a in range(-1,2):
                    for b in range(-1,2):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0

            # Top Left Corner Cell
            if i == 0 and j == 0:
                for a in range(0,2):
                    for b in range(0,2):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1
                                
                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0
               
            # Top Edge Cell
            if i == 0 and 0 < j < (len(state[i]) - 1):
                for a in range(0,2):
                    for b in range(-1,2):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0

            # Top Right Corner Cell
            if i == 0 and j == (len(state[i]) - 1):
                for a in range(0,2):
                    for b in range(-1,1):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0

            # Left Edge Cell
            if 0 < i < (len(state) - 1) and j == 0:
                for a in range(-1,2):
                    for b in range(0,2):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0

            # Right Edge Cell
            if 0 < i < (len(state) - 1) and j == (len(state[i]) - 1):
                for a in range(-1,2):
                    for b in range(-1,1):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0

            # Bottom Left Corner Cell
            if i == (len(state) - 1) and j == 0:
                for a in range(-1, 1):
                    for b in range(0, 2):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0

            # Bottom Edge Cell
            if i == (len(state) - 1) and 0 < j < (len(state[i]) - 1):
                for a in range(-1,1):
                    for b in range(-1,2):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0

            # Bottom Right Corner Cell
            if i == (len(state) - 1) and j == (len(state[i]) - 1):
                for a in range(-1,1):
                    for b in range(-1,1):
                        if a != 0 and b != 0:
                            if state[i + a][j + b] == 1:
                                liveCount = liveCount + 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] == 1
                else:
                    nextState[i][j] == 0
    return nextState
 '''


def next_board_state(state):
    nextState = state.copy()

    for i in range(len(state)):
        for j in range(len(state[i])):
            # Counter to keep track of alive neighbors
            liveCount = 0
            
            # Checks if cell is already alive
            if state[i][j] == 1:
                aliveCheck = True
            else:
                aliveCheck = False

            # Center Cell 
            if i > 0 and i < (len(state) - 1) and j > 0 and j < (len(state[i]) - 1):
                if state[i - 1][j - 1] == 1:
                    liveCount += 1
                if state[i - 1][j] == 1:
                    liveCount += 1
                if state[i - 1][j + 1] == 1:
                    liveCount += 1
                if state[i][j - 1] == 1:
                    liveCount += 1
                if state[i][j + 1] == 1:
                    liveCount += 1
                if state[i + 1][j - 1] == 1:
                    liveCount += 1
                if state[i + 1][j] == 1:
                    liveCount += 1
                if state[i + 1][j + 1] == 1:
                    liveCount += 1
            
                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

            # Top Left Corner Cell
            if i == 0 and j == 0:
                if state[i][j + 1] == 1:
                    liveCount += 1
                if state[i + 1][j] == 1:
                    liveCount += 1
                if state[i + 1][j + 1] == 1:
                    liveCount += 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0
                

        

            # Top Edge Cell
            if i == 0 and 0 < j < (len(state[i]) - 1):
                if state[i][j - 1] == 1:
                    liveCount += 1
                if state[i][j + 1] == 1:
                    liveCount += 1
                if state[i + 1][j - 1] == 1:
                    liveCount += 1
                if state[i + 1][j] == 1:
                    liveCount += 1
                if state[i + 1][j + 1] == 1:
                    liveCount += 1
                
                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

                

            # Top Right Corner Cell
            if i == 0 and j == (len(state[i]) - 1):
                if state[i][j - 1] == 1:
                    liveCount += 1
                if state[i + 1][j - 1] == 1:
                    liveCount += 1
                if state[i + 1][j] == 1:
                    liveCount += 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

            # Left Edge Cell
            if i > 0 and i < (len(state) - 1) and j == 0:
                if state[i - 1][j] == 1:
                    liveCount += 1
                if state[i - 1][j + 1] == 1:
                    liveCount += 1
                if state[i][j + 1] == 1:
                    liveCount += 1
                if state[i + 1][j] == 1:
                    liveCount += 1
                if state[i + 1][j + 1] == 1:
                    liveCount += 1

                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

            # Right Edge Cell
            if i > 0 and i < (len(state) - 1) and j == (len(state[i]) - 1):
                if state[i - 1][j - 1] == 1:
                    liveCount += 1
                if state[i - 1][j] == 1:
                    liveCount += 1
                if state[i][j - 1] == 1:
                    liveCount += 1
                if state[i + 1][j - 1] == 1:
                    liveCount += 1
                if state[i + 1][j] == 1:
                    liveCount += 1
              
                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

            # Bottom Left Corner Cell
            if i == (len(state) - 1) and j == 0:
                if state[i - 1][j] == 1:
                    liveCount += 1
                if state[i - 1][j + 1] == 1:
                    liveCount += 1
                if state[i][j + 1] == 1:
                    liveCount += 1
                
                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

            # Bottom Edge Cell
            if i == (len(state) - 1) and j > 0 and j < (len(state[i]) - 1):
                if state[i - 1][j - 1] == 1:
                    liveCount += 1
                if state[i - 1][j] == 1:
                    liveCount += 1
                if state[i - 1][j + 1] == 1:
                    liveCount += 1
                if state[i][j - 1] == 1:
                    liveCount += 1
                if state[i][j + 1] == 1:
                    liveCount += 1
               
                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

            # Bottom Right Corner Cell
            if i == (len(state) - 1) and j == (len(state[i]) - 1):
                if state[i - 1][j - 1] == 1:
                    liveCount += 1
                if state[i - 1][j] == 1:
                    liveCount += 1
                if state[i][j - 1] == 1:
                    liveCount += 1
                
                if is_alive(liveCount, aliveCheck) == True:
                    nextState[i][j] = 1
                else:
                    nextState[i][j] = 0

    return nextState


def is_alive(liveCount, isAlreadyAlive):
    # Death by underpopulation
    if liveCount < 2:
        return False
    # Alive - perfect conditions
    if 2 <= liveCount < 4 and isAlreadyAlive == True:
        return True
    # Death by overpopulation
    if liveCount >= 4:
        return False
    # Alive by reproduction
    if isAlreadyAlive == False and liveCount == 3:
        return True






initState = random_state(50,50)
render(initState)
nextState = next_board_state(initState)
while True:
    render(nextState) 
    nextState = next_board_state(nextState)
    time.sleep(.25)
    

