def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = [list(map(int, line.strip().split(', '))) for line in lines[:3]]
    gamma = float(lines[3].strip())
    threshold = float(lines[4].strip())
    rows = len(grid)
    cols = len(grid[0])

    return grid, gamma, threshold, 


grid, gamma, threshold,  = read_file('Q-Learning.txt')
print(grid)
print(gamma)
print(threshold)