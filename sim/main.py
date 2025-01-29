import sys

import arrangers
import testers as test
    

def named_model(name):
    '''
    Returns the arrangement function corresponding to the name
    '''
    if name == 'square_simple':
        return arrangers.square_simple
    if name == 'square_vertical':
        return arrangers.square_vertical
    if name == 'hexagonal':
        return arrangers.hexagonal
    if name == 'hexagonal_rotated':
        return arrangers.hexagonal_rotated
    else:
        sys.exit(f"Model {name} not found.")


if __name__ == '__main__':

    arrangement = 'hexagonal_rotated'
    resolution = 10
    
    df = test.test_general_arrangement(
        named_model(arrangement), 
        resolution, 
        save_figures=True
    )

    df.to_csv(f"data/{arrangement}_{resolution}.csv")