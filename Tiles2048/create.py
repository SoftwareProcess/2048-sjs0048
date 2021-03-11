import random

def _create(userParms):
    grid = '0200000000000020'
    locOne = random.randint(0, 15)
    locTwo = random.randint(0, 15)
    while locTwo == locOne:
        locTwo = random.randint(0,15)
    grid[locOne] = "2"
    grid[locTwo] = "2"
    
    result = {'grid': grid}
    return result
