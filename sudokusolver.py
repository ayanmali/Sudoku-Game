import numpy as np
from copy import copy, deepcopy

dim = 9

board = [

[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]

]

solvedBoard = deepcopy(board)

def isPossible(y, x, n):
    if solvedBoard[y][x] == 0:
        # determine which 3x3 grid the cell is in
        # check if that 3x3 grid doesnt have that number
    
        if 0 <= y <= 2:
            yVals = (0, 1, 2)
        elif 3 <= y <= 5:
            yVals = (3, 4, 5)
        elif 6 <= y <= 8:
            yVals = (6, 7, 8)

        if 0 <= x <= 2:
            xVals = (0, 1, 2)
        elif 3 <= x <= 5:
            xVals = (3, 4, 5)
        elif 6 <= x <= 8:
            xVals = (6, 7, 8)

        grid = [ solvedBoard[yVals[0]][xVals[0]:xVals[2]+1], solvedBoard[yVals[1]][xVals[0]:xVals[2]+1], solvedBoard[yVals[2]][xVals[0]:xVals[2]+1] ]
        
        for c in grid:
            for r in c:
                if n == r:
                    return False

        # check if the column doesnt have that number
        for c in range(dim):
            if solvedBoard[c][x] == n:
                return False

        # check if the row doesnt have that number
        for r in range(dim):
            if solvedBoard[y][r] == n:
                return False

        return True

def solve():
    
    for y in range(dim):
        for x in range(dim):
            if solvedBoard[y][x] == 0:
                for n in range(1, dim+1):
                    if isPossible(y, x, n):
                        solvedBoard[y][x] = n
                        if solve():
                            return True
                        # if the solution is not valid for this cell, set this cell to empty again and backtrack
                        solvedBoard[y][x] = 0
                
                return

    # if the solution for the current cell is valid, then move on to the next empty cell         
    return True

solve()

#print(np.matrix(board))

#print('\n')

#print(np.matrix(solvedBoard))

#print("\nDone")
