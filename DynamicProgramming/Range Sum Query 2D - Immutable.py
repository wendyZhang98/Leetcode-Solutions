### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0304.Range%20Sum%20Query%202D%20-%20Immutable/README.md



### Description:
# 给定一个二维矩阵，计算其子矩形范围内元素的总和
# 该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8



### Example:
# 给定 matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12



class Solution:

    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre[i][j] = self.pre[i - 1][j] \
                                 + self.pre[i][j - 1] \
                                 - self.pre[i - 1][j - 1] \
                                 + matrix[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        return self.pre[row2 + 1][col2 + 1] \
               - self.pre[row2 + 1][col1] \
               - self.pre[row1][col2 + 1] \
               + self.pre[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


print(Solution(matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],\
                         [1, 2, 0, 1, 5],[4, 1, 0, 1, 7],\
                         [1, 0, 3, 0, 5]]).sumRegion(2, 1, 4, 3))


print(Solution(matrix = [[3, 0, 1, 4, 2],[5, 6, 3, 2, 1],\
                         [1, 2, 0, 1, 5],[4, 1, 0, 1, 7],\
                         [1, 0, 3, 0, 5]]).sumRegion(1, 1, 2, 2))

