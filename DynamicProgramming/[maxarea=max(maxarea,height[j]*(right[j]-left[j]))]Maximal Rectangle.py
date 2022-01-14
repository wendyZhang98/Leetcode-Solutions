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





### Solution1:
# https://leetcode.com/problems/maximal-rectangle/solution/

### Dynamic Programming - Brute Force on Histograms
# We can compute the maximum width of a rectangle that ends at a given coordinate in constant time
# We do this by keeping track of the number of consecutive ones each square in each row
# As we iterate each row, we update the maximum possible width at that point
# This is done using row[i] = row[i-1] + 1 if row[i]=="1"

# Once we know the maximum widths for each point above a given point
# We can compute the maximum rectangle with the lower right corner at that point in linear time
# As we iterate up the column, we know that the maximum width of a rectangle 
# spanning from the original point to the current point is the running minimum of each maximal width we have encountered

# We define:
# maxWidth = min(maxWidth, widthHere)
# curArea = maxWidth * (currentRow - OriginalRow + 1)
# maxArea = max(maxArea, curArea)

# Repeating this process for every point in our input gives the global maximum

class Solution:
    def maximalRectangle(self, matrix):
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0': continue

                # compute the maximum width and update dp with it
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1

                # compute the maximum area rectangle with a lower right corner at [i, j]
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i-k+1))
        return maxarea

# Complexity Analysis:
# Time: O(NM N)
# Space: O(N M)





### Solution2:
# https://leetcode.com/problems/maximal-rectangle/solution/

### Dynamic Programming - Maximum Height at Each Point
# Imagine an algorithm where for each point we computed a rectangle by doing the following:
# Finding the maximum height of the rectangle by iterating upwards until a 0 is reached 
# Finding the maximum width of the rectangle by iterating outwards left and right until a height that doens't accommodate the maximum height of the rectangle
# We know that the maximum rectangle must be one of the rectangles constructed in this manner

# Algorithm:
# Given row matrix[i], we keep track of the h, l, and r of each point in the row by defining three arrays: height, left, and right
# height[j] will correspond to the height of matrix[i][j]
# and so on and so forth with the other arrays 

# The question now becomes how to update each array
# new_height[j] = old_height[j] + 1 if row[j]=="1" else 0

# Left: new_left[j] = max(old_left[j], cur_left)
# cur_left is one greater than rightmost occurence of zero we have encountered. 
# When we "expand" the rectangle to the left, we know it can't expand past that point, otherwise it'll run into the zero.

# Right: new_right[j] = min(old_right[j], cur_right)
# cur_right is the leftmost occurrence of zero we have encountered. 
# For the sake of simplicity, we don't decrement cur_right by one (like how we increment cur_left) 
# so we can compute the area of the rectangle with height[j] * (right[j] - left[j]) instead of height[j] * (right[j] + 1 - left[j]).
#This means that technically the base of the rectangle is defined by the half-open interval [l, r) instead of the closed interval [l, r],
# and right is really one greater than right boundary. 
# Although the algorithm will still work if we don't do this with right, doing it this way makes the area calculation a little cleaner.


class Solution:

    def maximalRectangle(self, matrix):
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n   # initialize left as the leftmost boundary possible
        right = [n] * n  # initialize right as the rightmost boundary possible
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
