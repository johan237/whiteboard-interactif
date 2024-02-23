
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = [list(map(int, line.strip().split(', '))) for line in lines[:3]]
    gamma = float(lines[3].strip())
    alpha = float(lines[4].strip())
    rows = len(grid)
    cols = len(grid[0])
    return grid,gamma,alpha


grid, gamma , alpha = read_file("file.txt")

actions = {
    0: "up" ,
    1: "down" ,
    2: "left" ,
    3: "right" 
}
# print(grid)

# Initializing starting position of pacman in matrix

starting_state = [2,0]

# Define a state dictionary to store information for all the possible states in the pacman game, their reward, are they terminal ?, current_V(s)
# stateDict  = [ [
#     {"utility": 0, "bestAction":"none", "reward": ( lambda : -0.04 if grid[i][j] ==0 else (1 if grid[i][j] == 1 else (-1 if grid[i][j] ==2 else 0)))()   } 
#         for j in range(4) ] for i in range(3)]

qTable = [ [ [ 0 for i in range(4)] for j in range(4)] for k in range(3)]


rewards  = [ [ ( lambda : -0.04 if grid[i][j] ==0 else (1 if grid[i][j] == 1 else (-1 if grid[i][j] ==2 else 0)))()   
        for j in range(4) ] for i in range(3)]


epsilon = 9

def epsilon_greedy():
    number = random.randint(1,10)
    if number <= 9:
        # exploit
        q_table = qTable[2][0]
        action_value  = q_table.index(max(q_table))
    else:
        # explore
         action_value = random.randint(0, 3)  # between 0 and 4 to choose between up, left, right and down    


def qfunction():
    start = [2,0]
    action_value = epsilon_greedy()
    action = actions[action_value]
    q_table = qTable[2][0]
    qTable[2][0][action_value] += alpha * (rewards[2][0] + gamma* np.max(Q[next_state, :]) - Q[state, action])
