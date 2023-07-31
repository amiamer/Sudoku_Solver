# Sudoku Solver

This is a Python implementation of a Sudoku solver using a backtracking algorithm. Given a 9x9 Sudoku puzzle as input, the solver attempts to find a valid solution, modifying the puzzle in place if successful. If no solution exists, the solver returns `False`.

## Table of Contents

- [Introduction](#sudoku-solver)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## How It Works

Sudoku is a logic-based number-placement puzzle. The objective is to fill a 9x9 grid with digits from 1 to 9, ensuring that each row, each column, and each of the nine 3x3 subgrids (also called regions or boxes) contain all the digits from 1 to 9, with no repetition.

The solver uses a backtracking algorithm to explore all possible solutions by placing numbers in empty cells and recursively validating the puzzle. If a number violates any Sudoku rules, it backtracks and tries a different number. This process continues until a valid solution is found or all possibilities are exhausted.

## Requirements

- Python 3.x

## Installation

Clone this repository to your local machine:

    git clone https://github.com/amiamer/Sudoku_Solver.git

## Usage

1. Ensure you have Python 3.x installed on your system.

2. Import the `solveSudoku` function from `sudoku_solver.py` into your project.

3. Create a 9x9 Sudoku puzzle board represented as a list of lists, where empty cells are denoted by the value `0`.

4. Call the `solveSudoku` function with the puzzle board as the argument.

5. The function will attempt to solve the puzzle in place. If a solution is found, the puzzle will contain the solved configuration. If no solution exists, the puzzle will remain unchanged.

## Code Explanation

- `findNextEmpty`: Finds the next empty cell (cell containing 0) in the puzzle.

- `isValid`: Checks whether it's valid to place a number (guess) in a given cell (row, col) of the puzzle.

- `solveSudoku`: The main recursive function that attempts to solve the Sudoku puzzle using backtracking. It places valid numbers in empty cells, recursively calls itself, and backtracks if no valid number can be placed.

## Example

```python
from sudoku_solver import solveSudoku

exampleBoard = [
    [9, 7, 0, 0, 0, 0, 0, 8, 0],
    [3, 0, 0, 0, 5, 9, 6, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 1, 0, 0],
    [4, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 4, 1, 0, 0, 7],
    [0, 0, 0, 0, 0, 2, 0, 0, 0],
    [5, 0, 0, 0, 1, 3, 9, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 0, 6]
]

if solveSudoku(exampleBoard):
    print("Sudoku puzzle solved successfully!")
    # Print the solved puzzle board
else:
    print("No solution exists for the given Sudoku puzzle.")
    # The puzzle remains unchanged

