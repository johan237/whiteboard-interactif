from readingFile import read_file, addTrace

grid, gamma, threshold = read_file("file.txt")

actions = {
    "up" :0,
    "down" :1,
    "left" :2,
    "right" :3
}
# print(grid)

# Initializing starting position of pacman in matrix

starting_state = [2,0]

# Define a state dictionary to store information for all the possible states in the pacman game, their reward, are they terminal ?, current_V(s)
# stateDict  = [ [
#     {"utility": 0, "bestAction":"none", "reward": ( lambda : -0.04 if grid[i][j] ==0 else (1 if grid[i][j] == 1 else (-1 if grid[i][j] ==2 else 0)))()   } 
#         for j in range(4) ] for i in range(3)]

qTable = [ [ [ 0 for i in range(4)] for j in range(4)] for k in range(3)]

print(qTable)


epsilon = 0.9

def epsilon_greedy():
    number = random.randint()
    if number <= 0.9:
        # exploit
        # action  = choose_action_with_largest_reward
        print('Hello world')
    else:
         action = random.randint(0, 4)  # between 0 and 4 to choose between up, left, right and down
    