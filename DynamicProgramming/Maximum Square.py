# https://leetcode.com/problems/maximal-square/




### Description:
# Given a m*n binary matrix filled with 0's and 1's 
# Find the largest square containing only 1's and return its area




### Examples:
# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4

# Input: matrix = [["0","1"],["1","0"]]
# Output: 1

# Input: matrix = [["0"]]
# Output: 0




### Solution:
# Start from index (0,0)
# For every 1 found in the original matrix 
# We update the value of the current element as:
# dp[i,j] = min(dp[i-1,j], dp[i-1,j-1], dp[i,j-1])+1
# We also remember the size of the largest square found so far
# In this way, we traverse the original matrix once and find out the required maximum size

# https://leetcode.com/problems/maximal-square/discuss/1632145/C%2B%2BJAVAPYTHON-EASY-TO-SOLVE-oror-Detailed-Explanation-of-DP-with-Visualization-and-dry-run


class Solution:
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        
        maxSqr = 0
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1 
                    maxSqr = max(maxSqr, dp[i+1][j+1])
                
        return maxSqr * maxSqr

print(Solution().maximalSquare(matrix=[["1","0","1","0","0"],\
                                       ["1","0","1","1","1"],\
                                       ["1","1","1","1","1"],\
                                       ["1","0","0","1","0"]]))

# Time Comlexity: O(mn)
# Space Complexity: O(mn)
