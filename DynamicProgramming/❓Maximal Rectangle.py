# https://leetcode.com/problems/maximal-rectangle/




### Description:
# Given a [rows x cols] binary matrix filled with 0's and 1's 
# find the largest rectangle containing only 1's and return its area




### Example:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1




### Solution:
# https://leetcode.com/problems/maximal-rectangle/solution/

# Dynamic Programming - Maximum Height at Each Point
# Imagine an algorithm where for each point we computed a rectangle by doing the following:
# Finding the maximum height of the rectangle by iterating upwards until a 0 is reached 
# Finding the maximum width of the rectangle by iterating outwards left and right until a height that doens't accommodate the maximum height of the rectangle
# We know that the maximum rectangle must be one of the rectangles constructed in this manner

# Algorithm:
# Given a maximum rectangle with height h, left bound l, right bound r
# Given row matrix[i], we keep track of the h, l, and r of each point in the row by defining three arrays: height, left, and right
# height[j]: height of matrix[i][j]
# so on and so forth with the other arrays 

# The question now becomes how to update each array
# Height: row[j] = row[j-1] + 1 if row[j]=="1"
# new_height[j] = old_height[j] + 1 if row[j]=="1" else 0

# Left: new_left[j] = max(old_left[j], cur_left)
# cur_left is one greater than rightmost occurence of zero we have encountered. 

# Right: new_right[j] = min(old_right[j], cur_right)
# cur_right is the leftmost occurence of zero we have encountered.

class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0

        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea
