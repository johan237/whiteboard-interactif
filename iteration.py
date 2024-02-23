from fun1 import extract_optimal_path, read_file



file_path = 'Q-Learning.txt'
grid, gamma, threshold, S = read_file(file_path)
A = list(range(4))





def P(s_next, s, a, grid, rows, cols):
    # Calculate the intended next state based on the action
    intended_next_state = None
    if a == 0:  # Up
        intended_next_state = s - cols if s - cols >= 0 else s
    elif a == 1:  # Right
        intended_next_state = s + 1 if (s + 1) % cols != 0 else s
    elif a == 2:  # Down
        intended_next_state = s + cols if s + cols < rows * cols else s
    elif a == 3:  # Left
        intended_next_state = s - 1 if s % cols != 0 else s

    # Check if the intended next state is blocked
    if grid[intended_next_state // cols][intended_next_state % cols] == -1:
        intended_next_state = s  # Stay in the same state if blocked

    # Calculate the probability of reaching s_next
    if s_next == intended_next_state:
        return 0.8
    elif s_next == s:
        return 0.1 * (4 - 1)  # 10% chance to stay for each of the 3 other directions
    else:
        # Check for orthogonal directions
        orthogonal_states = [s - cols, s + 1, s + cols, s - 1]
        if intended_next_state in orthogonal_states:# Up, Right, Down, Left
            orthogonal_states.remove(intended_next_state)  # Remove the intended direction
        if s_next in orthogonal_states:
            return 0.1  # 10% chance to move in an orthogonal direction

    return 0.0


def R(s, grid, cols):
    # Check the state type based on the grid
    if grid[s // cols][s % cols] == 2:
        return -1  # Monster
    elif grid[s // cols][s % cols] == 1:
        return 1  # Goal
    elif grid[s // cols][s % cols] == 0:
        return -0.04  # Free state
    else:
        return 0  # Default reward for undefined cases

def value_iteration(S, A, grid, gamma, threshold, R, P, start_state):
    rows = len(grid)
    cols = len(grid[0])
    V = {s: 0 for s in S}
    policy = {s: None for s in S}

    while True:
        delta = 0
        for s in S:
            Q = {a: R(s, grid, cols) + gamma * sum(P(s_next, s, a, grid, rows, cols) * V[s_next] for s_next in S) for a in A}
            best_action = max(Q, key=Q.get)
            best_value = Q[best_action]
            delta = max(delta, abs(V[s] - best_value))
            V[s] = best_value
            policy[s] = best_action

        if delta <= threshold:
            break

    optimal_path = extract_optimal_path(policy, start_state)

    print(optimal_path)

# Call value_iteration with optimized functions and parameters
value_iteration(S, A, grid, gamma, threshold, R, P, 8)


print("heejhi")