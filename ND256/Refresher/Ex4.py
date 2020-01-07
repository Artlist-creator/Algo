correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]

# Define a function check_sudoku() here:


def check_sudoku(sudoku_grid):
    for row in sudoku_grid:
        if len(row) != len(set(row)):
            print('f1')
            return False
    length = len(sudoku_grid)
    col_set = set()
    for col in range(len(sudoku_grid[0])):
        for i in range(length):
            if (not str(sudoku_grid[i][col]).isdigit() or sudoku_grid[i][col] > length):
                print('f2')
                return False
            col_set.add(sudoku_grid[i][col])
        if (len(col_set) != len(sudoku_grid)):
            print('f3')
            return False
        col_set.clear()
    return True


print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False 
