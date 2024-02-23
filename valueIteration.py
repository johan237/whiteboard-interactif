from readingFile import read_file 
import numpy as np

actions = {
    "up": {
        "adjacent": ["left", "right"]
        },
    "down": {
        "adjacent": ["left", "right"]
        },
    "left": {
        "adjacent": ["up", "down"]
        },
    "right": {
        "adjacent": ["up", "down"]
        },
}


# Extracting all possible positions in file and corresponding meaning 
# grid = np.genfromtxt("file.txt", delimiter=',')
grid, gamma, threshold = read_file("file.txt")
print(grid)

# Initializing starting position of pacman in matrix

starting_state = [2,0]

# Define a state dictionary to store information for all the possible states in the pacman game, their reward, are they terminal ?, current_V(s)
stateDict  = [ [
    {"utility": 0, "bestAction":"none", "reward": ( lambda : -0.04 if grid[i][j] ==0 else (1 if grid[i][j] == 1 else (-1 if grid[i][j] ==2 else 0)))()   } 
        for j in range(4) ] for i in range(3)]

temp_dict = [[( lambda : -0.04 if grid[i][j] ==0 else (1 if grid[i][j] == 1 else (-1 if grid[i][j] ==2 else 0)))() for j in range(4)] for i in range(3)]
temporalData = [ [0,0,0,0] for j in range(3)]

print(stateDict)
print(temp_dict)



# Find a way to loop through all possible actions from state current_position and for each action, calculate Q(current_position,action)



# def reward_in_state(state, action, next_state):
    

def Qvalue(state, action):
    utility  = 0
    if(action == "up" or action == "down"): 
        utility += calculate(transition(state,action),0.8)
        utility += calculate(transition(state,"left"),0.1)
        utility += calculate(transition(state,"right"),0.1)
    
    if(action == "left" or action == "right"):
        utility += calculate(transition(state,action),0.8)
        utility += calculate(transition(state,"up"),0.1)
        utility += calculate(transition(state,"down"),0.1)

    next_state   = transition(state,action)
    return [utility, next_state, action]


def calculate(state, probability):
    return probability * (stateDict[state[0]][state[1]]["reward"] + (gamma * stateDict[state[0]][state[1]]["utility"]) )

# move()

def is_Wall(position):
    return (grid[position[0]][position[1]] == 3)

def final_position( new_position, old_position):
    return old_position if is_Wall(new_position) else new_position 

def transition(state, action):
    current_row = state[0]
    current_column = state[1]
    if(action == "up"):
        return final_position([( lambda : current_row if (state[0]-1) <=-1 else state[0]-1  )(), current_column], 
                              state)
    if(action == "down"):
        return final_position([( lambda : current_row if (current_row+1) >=3 else current_row+1  )(), current_column], 
                              state)
    if(action == "left"):
        return final_position([ current_row, ( lambda : current_column if (current_column-1) <=-1 else current_column-1  )() ],  
                              state)
    if(action == "right"):
        return final_position( [ current_row , ( lambda : current_column if (current_column+1) >=4 else current_column+1  )() ],   
                              state)

def setUtility(state, utility):
    stateDict[state[0]][state[1]]["utility"] = utility
    temporalData[state[0]][state[1]] = utility
    temp_dict[state[0]][state[1]] =utility
    return

def convergence():
    # calculate the absolute difference between previous utility with current utility
    return 1;

def value_iterate():
     
    # value ,next_state  =    max(values, key=lambda x: x[1]
    current_state = [2,0]
    all_actions_taken  = ["Start"]
    count = 1
    while (count != 30) :
        allQValues = [
            Qvalue(current_state, "up"),
            Qvalue(current_state, "down"),
            Qvalue(current_state, "left"),
            Qvalue(current_state, "right"),
            ]
        current_state_utility = stateDict[current_state[0]][current_state[1]]["utility"]
        if(current_state_utility == 1) : 
            print('******Reached End state********')
            break
        maxQValueArray = max(allQValues, key=lambda x: x[0])
        utility, next_state, action  = maxQValueArray
        difference  = abs(utility - current_state_utility)
        # if(difference <= epsilon) : break 
        # print(allQValues)
        #  [current_state_utility, current_state, action]
        action_taken = action + "[" + str(next_state[0]) + " " + str(next_state[1]) + "]"
        print(allQValues)
        all_actions_taken.append(action)
        setUtility(current_state, utility)
        current_state =  next_state
        count = count + 1
    print(all_actions_taken)
    
    print('End ')
    # for row in temp_dict:
    #     print(row)

for i in range(4):
    value_iterate()
    for row in temp_dict:
        print(row)
# for row in temp_dict:
#         print(row)

'''
0,0,0,1
0,3,0,2
0,0,0,0

[3][0]

0  1  2  3
4  5  6  7
8  9  10 11

'''


'''
TODO: The agent fallbacks too much in thesame state even though he should change path since the current path is faulty\
    

'''