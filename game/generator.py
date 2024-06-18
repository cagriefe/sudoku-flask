import random
import numpy as np


# in easy mode %45-%50 will be available 
#%30-%40 in hard
#%20-%30 in expert


def generate_sudoku():
    grid = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]
    
    total_cells = 9 * 9
    num_zeros = int(total_cells * 0.55)
    positions = list(range(total_cells))
    random.shuffle(positions)
    
    for i in range(num_zeros):
        row = positions[i] // 9
        col = positions[i] % 9
        grid[row][col] = 0
    
    return grid

random_grid = generate_sudoku()

for row in random_grid:
    print(row)