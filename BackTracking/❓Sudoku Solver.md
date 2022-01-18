https://leetcode.com/problems/sudoku-solver/



### Description:
- Write a program to solve a Sudoku puzzle by filling the empty cells.
- A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
- The '.' character indicates empty cells.



### Examples:
<img width="1267" alt="Screen Shot 2022-01-18 at 11 02 59" src="https://user-images.githubusercontent.com/49216429/149973367-de30b7a5-6d78-408e-938d-c2c5e536ebcb.png">



### Solutions:
<img width="844" alt="Screen Shot 2022-01-18 at 11 03 45" src="https://user-images.githubusercontent.com/49216429/149973516-0dba163f-0528-460f-af6b-b42594718bb8.png">
<img width="996" alt="Screen Shot 2022-01-18 at 11 10 28" src="https://user-images.githubusercontent.com/49216429/149974656-49122c50-111c-49e6-babd-12c2e37084d8.png">
<img width="984" alt="Screen Shot 2022-01-18 at 11 30 54" src="https://user-images.githubusercontent.com/49216429/149978203-8a1460a2-c403-4876-8599-d59e9c234581.png">
<img width="995" alt="Screen Shot 2022-01-18 at 11 32 19" src="https://user-images.githubusercontent.com/49216429/149978451-42b95589-1426-45e1-ae23-9ecd72f4dab0.png">
<img width="985" alt="Screen Shot 2022-01-18 at 11 50 41" src="https://user-images.githubusercontent.com/49216429/149981748-4ffd8263-90f8-4fd9-bae6-df8026cc4801.png">

```
from collections import defaultdict
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def could_place(d, row, col):
            """
            Check if one could place a number d in (row, col) cell
            """
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])
        
        def place_number(d, row, col):
            """
            Place a number d in (row, col) cell
            """
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
            
        def remove_number(d, row, col):
            """
            Remove a number which didn't lead 
            to a solution
            """
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
            
        def place_next_numbers(row, col):
            """
            Call backtrack function in recursion
            to continue to place numbers
            till the moment we have a solution
            """
            # if we're in the last cell
            # that means we have the solution
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True
            #if not yet    
            else:
                # if we're in the end of the row
                # go to the next row
                if col == N - 1:
                    backtrack(row + 1, 0)
                # go to the next column
                else:
                    backtrack(row, col + 1)
                
                
        def backtrack(row = 0, col = 0):
            """
            Backtracking
            """
            # if the cell is empty
            if board[row][col] == '.':
                # iterate over all numbers from 1 to 9
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:
                            remove_number(d, row, col)
            else:
                place_next_numbers(row, col)
                    
        # box size
        n = 3
        # row size
        N = n * n
        # lambda function to compute box index
        box_index = lambda row, col: (row // n ) * n + col // n
        
        # init rows, columns and boxes
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()
```
