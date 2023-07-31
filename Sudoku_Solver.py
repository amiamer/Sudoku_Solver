from pprint import pprint

def findNextEmpty(puzzle):
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == 0:
                return r, c
    
    return None, None

def isValid(puzzle, guess, row, col):
    rowValues = puzzle[row]
    if guess in rowValues:
        return False

    colValues = [puzzle[i][col] for i in range(9)]
    if guess in colValues:
        return False
    
    rowStart = (row // 3) * 3
    colStart = (col // 3) * 3

    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True
    

def solveSudoku(puzzle):
    row, col = findNextEmpty(puzzle)

    if row is None:
        return True

    for guess in range(1,10):
        if isValid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solveSudoku(puzzle):
                return True
            
        puzzle[row][col] = 0
    
    return False

if __name__ == '__main__':
    exampleBoard = [
        [9, 7, 0,   0, 0, 0,   0, 8, 0],
        [3, 0, 0,   0, 5, 9,   6, 0, 0],
        [0, 0, 0,   4, 0, 0,   0, 0, 0],

        [0, 0, 0,   2, 0, 0,   1, 0, 0],
        [4, 0, 0,   6, 0, 0,   0, 0, 0],
        [0, 3, 0,   0, 4, 1,   0, 0, 7],

        [0, 0, 0,   0, 0, 2,   0, 0, 0],
        [5, 0, 0,   0, 1, 3,   9, 0, 0],
        [0, 0, 9,   0, 0, 0,   0, 0, 6]
    ]
    print(solveSudoku(exampleBoard))
    pprint(exampleBoard)
