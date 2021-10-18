### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0063.Unique%20Paths%20II/README.md


### Description:
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）
# 机器人每次只能向下或者向右移动一步
# 机器人试图达到网格的右下角（在下图中标记为“Finish”）
# 现在考虑网格中有障碍物
# 那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。


### Example:
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1


### Solution:
# 动态规划
# 假设 dp[i][j] 表示到达网格 (i,j) 的路径数，先初始化 dp 第一列和第一行的所有值，然后判断
# 若 obstacleGrid[i][j] == 1，说明路径数为 0，dp[i][j] = 0
# 若 obstacleGrid[i][j] == 0，则 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
# 最后返回 dp[m - 1][n - 1] 即可


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # m: row
        # n: column
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


print(Solution().uniquePathsWithObstacles(obstacleGrid=[[0,1],[0,0]]))

print(Solution().uniquePathsWithObstacles(obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]))
