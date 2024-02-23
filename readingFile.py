def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = [list(map(int, line.strip().split(', '))) for line in lines[:3]]
    gamma = float(lines[3].strip())
    threshold = float(lines[4].strip())
    rows = len(grid)
    cols = len(grid[0])

    return grid, gamma, threshold, 


def addTrace(steps, file_path):
    try:
        with open(file_path, 'a') as file:
            file.write('->'.join(steps) + '\n')
    except IOError:
        print(f'Error: Could not open or write to the file {file_path}.')