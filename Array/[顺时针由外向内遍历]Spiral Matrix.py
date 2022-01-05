# Link：
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0054.Spiral%20Matrix/README.md


### Description：
# 给你一个 m 行 n 列的矩阵 matrix，
# 请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。


### Example：
# 示例 1：
# 输入：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 输出：[1, 2, 3, 6, 9, 8, 7, 4, 5]

# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]


### Solution：
# 从外往里一圈一圈遍历并存储矩阵元素即可


# https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/

class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order
