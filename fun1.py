def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = [list(map(int, line.strip().split(', '))) for line in lines[:3]]
    gamma = float(lines[3].strip())
    threshold = float(lines[4].strip())
    rows = len(grid)
    cols = len(grid[0])
    S = [i for i in range(rows * cols)]

    return grid, gamma, threshold, S

file_path = 'Q-Learning.txt'
grid, gamma, threshold, S = read_file(file_path)


def get_next_state(current_state, action, grid):
    rows = len(grid)
    cols = len(grid[0])
    next_state = current_state

    if action == 0:  # Up
        next_state = current_state - cols if current_state // cols > 0 else current_state
    elif action == 1:  # Right
        next_state = current_state + 1 if (current_state + 1) % cols != 0 else current_state
    elif action == 2:  # Down
        next_state = current_state + cols if current_state // cols < rows - 1 else current_state
    elif action == 3:  # Left
        next_state = current_state - 1 if current_state % cols > 0 else current_state

    # Check if the next state is blocked
    if grid[next_state // cols][next_state % cols] == 3:
        next_state = current_state  # Stay in the same state if blocked

    return next_state


def is_terminal_state(state, grid):
    # Assuming the terminal states are marked as 1 (goal) and -1 (monster) in the grid
    rows = len(grid)
    cols = len(grid[0])

    if grid[state // cols][state % cols] in [2, 1]:
        return True  # The state is a terminal state
    else:
        return False  # The state is not a terminal state


def extract_optimal_path(policy, start_state):
    current_state = start_state
    optimal_path = []

    while True:
        action = policy[current_state]
        optimal_path.append((current_state, action))

        if is_terminal_state(current_state, grid):
            break

        current_state = get_next_state(current_state, action, grid)

    return optimal_path