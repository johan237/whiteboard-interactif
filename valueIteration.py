import numpy as np
'''
 - return the position of all elements in file
 
 function value_iteration(file_input):
    # Initialize the value function to zero for all states
    value_function = [0 for i in range(num_states)]
    
    # Set the convergence threshold and maximum number of iterations
    threshold = 0.001
    max_iterations = 1000
    
    # Iterate until convergence or maximum number of iterations is reached
    for i in range(max_iterations):
        # Initialize the delta value to zero
        delta = 0
        
        # Iterate over all states
        for state in range(num_states):
            # Initialize the new value function value to the current value function value
            new_value = value_function[state]
            
            # Check if the state is a reward state, goal state, monster state, or wall state
            if state == reward_state:
                new_value = 1
            elif state == goal_state:
                new_value = 0
            elif state == monster_state:
                new_value = -1
            elif state == wall_state:
                new_value = value_function[prev_state]
            
            # Iterate over all possible actions
            for action in range(num_actions):
                # Initialize the expected value to zero
                expected_value = 0
                
                # Calculate the expected value of the next state
                for next_state in range(num_states):
                    # Calculate the probability of transitioning to the next state
                    probability = transition_probability(state, action, next_state)
                    
                    # Calculate the value of the next state
                    next_value = value_function[next_state]
                    
                    # Add the product of the probability and the value of the next state to the expected value
                    expected_value += probability * next_value
                
                # Calculate the new value of the current state
                new_value = max(new_value, expected_value)
                
                # Update the delta value if the new value is greater than the current value
                delta = max(delta, abs(new_value - value_function[state]))
            
            # Update the value function with the new value
            value_function[state] = new_value
        
        # Check if convergence has been reached
        if delta < threshold:
            break
    
    # Return the value function
    return value_function

'''

file  = open("file.txt", "r")
gamma = 0.5
epsilon = 0.2

my_array = np.genfromtxt("file.txt", delimiter=',')

currentPosition = my_array[2][0]

# move()

num_states = 3
value_function = [[0,0,0] for i in range(num_states)]

print(value_function)


'''
0,0,0,1
0,3,0,2
0,0,0,0

[3][0]

0  1  2  3
4  5  6  7
8  9  10 11

'''
actions = {
    "up": 0,
    "down": 1,
    "left": 2,
    "right": 3,
    "none": -1
}

stateDict  = [[{"value": 0, "bestAction":"none", "reward": ( lambda : -0.04 if my_array[j][i] ==0 else (1 if my_array[j][i] == 1 else -1))()   } for i in range(4) ] for j in range(3)]

print(stateDict)


def QFunction(s,a):
    match a:
        case 0:
            return value_function[s][0]
        case 1:
            return value_function[s][1]
        case 2:
            return value_function[s][2]
        case 3:
            return value_function[s][3]
    
    for i in range(3):
        for j in range(3):
            if stateDict[i][j]["value"] == s:
                return stateDict[i][j]["bestAction"]
    



def move(currentI, currentJ):

 result = []
#  left
 result.append([--currentI,])
[[0,0,0] for i in range(num_states)]

thislist = ["apple", "banana", "cherry"]
thislist.append([1,2,3])
a  = 2
print(thislist[3][(--a)])