from main import next_board_state
from main import render

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors should stay dead
    '''
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    actual_next_state1 = next_board_state(init_state1)

    test1Passed = True
    for i in range(len(init_state1)):
        for j in range(len(init_state1[i])):
            if expected_next_state1[i][j] != actual_next_state1[i][j]:
                test1Passed = False
           
    if test1Passed == False:
        print("TEST 1: FAILED")
        print("Expected:")
        render(expected_next_state1)
        print("Actual:")
        render(actual_next_state1)
    else: 
        print("TEST 1: PASSED")
    '''
    # TEST 2: dead cells with exactly 3 neighbors should come alive

    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]

    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]

    actual_next_state2 = next_board_state(init_state2)

    render(actual_next_state2)

    test2Passed = True
    for i in range(len(init_state2)):
        for j in range(len(init_state2[i])):
            if expected_next_state2[i][j] != actual_next_state2[i][j]:
                test2Passed = False

    if test2Passed == False:
        print("TEST 2: FAILED")
        print("Expected:")
        render(expected_next_state2)
        print("Actual:")
        render(actual_next_state2)
    else:
        print("TEST 2: PASSED")

           

