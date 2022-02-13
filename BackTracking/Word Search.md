### Description:
- Given an m x n grid of characters board and a string word, return true if word exists in the grid.
- The word can be constructed from letters of sequentially adjacent cells, 
- where adjacent cells are horizontally or vertically neighboring. 
- The same letter cell may not be used more than once.



### Examples:
<img width="838" alt="Screen Shot 2022-02-12 at 23 08 37" src="https://user-images.githubusercontent.com/49216429/153738199-f80e3e21-5bd3-475b-8822-2475135f59a7.png">



### Solution:
<img width="831" alt="Screen Shot 2022-02-12 at 23 27 24" src="https://user-images.githubusercontent.com/49216429/153738600-69633395-c616-4259-9fc6-e7cecf7754a1.png">

<img width="832" alt="Screen Shot 2022-02-12 at 23 28 09" src="https://user-images.githubusercontent.com/49216429/153738617-d8d470c2-b2ff-4fba-8eb7-e1ec3acf09a4.png">

```
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret
```
