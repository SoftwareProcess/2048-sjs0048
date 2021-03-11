import random

def _create(userParms):
    initial = '0000000000000000'
    locOne = random.randint(0, 15)
    locTwo = random.randint(0, 15)
    while locOne == locTwo:
        locTwo = random.randint(0,15)
    translation = list(initial)
    translation[locOne] = '2'
    translation[locTwo] = '2'
    grid = str(translation)
    
    result = {'grid': grid, 'pos1': locOne, 'pos2': locTwo}
    return result
