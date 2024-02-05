import numpy as np

file  = open("file.txt", "r")
gamma = 0.5
epsilon = 0.2

actions = {
    "up": {
        "adjacent": ["left", "right"]
        },
    "down": {
        "adjacent": ["left", "right"]
        },
    "left": {
        "adjacent": ["left", "right"]
        },
    "right": 3
}


# Extracting all possible positions in file and corresponding meaning 
my_array = np.genfromtxt("file.txt", delimiter=',')

# Initializing starting position of pacman in matrix

starting_state = [2,0]

# Define a state dictionary to store information for all the possible states in the pacman game, their reward, are they terminal ?, current_V(s)
stateDict  = [ [
    {"value": 0, "bestAction":"none", "reward": ( lambda : -0.04 if my_array[i][j] ==0 else (1 if my_array[i][j] == 1 else (-1 if my_array[i][j] ==2 else 0)))()   } 
        for j in range(4) ] for i in range(3)]

temp_dict = [[( lambda : -0.04 if my_array[i][j] ==0 else (1 if my_array[i][j] == 1 else -1))() for j in range(4)] for i in range(3)]
temporalData = [ [0,0,0,0] for j in range(3)]

print(stateDict)
print(temp_dict)



# Find a way to loop through all possible actions from state current_position and for each action, calculate Q(current_position,action)


def Qvalue(state, action):
    # print('Inside QValue state is ', state)
    # print("Inside QValue Action is ",  action)
    value  = 0
    if(action == "up" or action == "down"): 
        # print("Action is indeed up or down", action, )  
        value += calculate(explore(state,action),0.8)
        value += calculate(explore(state,"left"),0.1)
        value += calculate(explore(state,"right"),0.1)
    
    if(action == "left" or action == "right"):
        # print("Action is indeed left or right", action)  

        value += calculate(explore(state,action),0.8)
        value += calculate(explore(state,"up"),0.1)
        value += calculate(explore(state,"down"),0.1)

    next_state   = explore(state,action)
    return [value, next_state, action]


def calculate(state, probability):
    return probability * (stateDict[state[0]][state[1]]["reward"] + (gamma * stateDict[state[0]][state[1]]["value"]) )

# move()

def is_Wall(position):
    return (my_array[position[0]][position[1]] == 3)

def final_position( new_position, old_position):
    return old_position if is_Wall(new_position) else new_position 

def explore(state, action):
    current_row = state[0]
    current_column = state[1]
    # print('In explore function')
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

def setValue(state, value):
    stateDict[state[0]][state[1]]["value"] = value
    temporalData[state[0]][state[1]] = value
    temp_dict[state[0]][state[1]] =value
    return

def value_iterate():
     
    # value ,next_state  =    max(values, key=lambda x: x[1]
    current_state = [0,2]
    all_actions_taken  = ["Start"]
    count = 1
    while (count != 20) :
        print('RUNNING FOR THE ',count,"th time")
        print(current_state)
        print(not(stateDict[current_state[0]][current_state[1]]['reward'] == 1 or stateDict[current_state[0]][current_state[1]]['reward'] == -1))
        allQValues = [
            Qvalue(current_state, "up"),
            Qvalue(current_state, "down"),
            Qvalue(current_state, "left"),
            Qvalue(current_state, "right")
            ]

        maxQValueArray = max(allQValues, key=lambda x: x[0])
        maxQValue, next_state, action  = maxQValueArray
        all_actions_taken.append(action)
        setValue(current_state, maxQValue)
        current_state =  next_state
        count = count + 1
    print(all_actions_taken)
    for row in temp_dict:
        print(row)

value_iterate()

'''
0,0,0,1
0,3,0,2
0,0,0,0

[3][0]

0  1  2  3
4  5  6  7
8  9  10 11

'''