def checkvalid(row, col, number, grid):
    # Check row
    for x in range(9):
        if grid[row][x] == number:
            return False

    # Check column
    for x in range(9):
        if grid[x][col] == number:
            return False

    # Check 3x3 sub-grid
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True


def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, 10):
        if checkvalid(row, col, num, grid):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
            grid[row][col] = 0

    return False  # Moved outside the for loop


grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

if solve(grid, 0, 0):
    for i in range(9):
        print(grid[i])
else:
    print("No solution available / the Sudoku you entered is invalid")
