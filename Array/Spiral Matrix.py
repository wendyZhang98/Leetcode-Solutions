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


###
class Solution:
    def spiralOrder(self, matrix):
        def add(i1, j1, i2, j2):
            if i1 == i2:
                return [matrix[i1][j] for j in range(j1, j2 + 1)]
            if j1 == j2:
                return [matrix[i][j1] for i in range(i1, i2 + 1)]
            return [matrix[i1][j] for j in range(j1, j2)] + [matrix[i][j2] for i in range(i1, i2)] + [matrix[i2][j] for j in range(j2, j1, -1)] + [matrix[i][j1] for i in range(i2, i1, -1)]
        m, n = len(matrix), len(matrix[0])
        i1, j1, i2, j2 = 0, 0, m - 1, n - 1
        res = []
        while i1 <= i2 and j1 <= j2:
            res += add(i1, j1, i2, j2)
            i1, j1, i2, j2 = i1 + 1, j1 + 1, i2 - 1, j2 - 1
        return res
