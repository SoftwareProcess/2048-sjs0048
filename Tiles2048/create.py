import random

def _create(userParms):
    initial = '0000000000000000'
    locOne = random.randint(0, 15)
    locTwo = random.randint(0, 15)
    grid = list(initial)
    grid[locOne] = '2'
    grid[locTwo] = '2'
    grid = str(grid)
    
    result = {'grid': grid}
    return result
