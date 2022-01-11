### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0064.Minimum%20Path%20Sum/README.md




### Requirement:
# 给定一个包含非负整数的 m x n 网格 grid
# 请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小
# 说明：每次只能向下或者向右移动一步

# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小

# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12




### Solution:
# 动态规划
# 假设 dp[i][j] 表示到达网格 (i,j) 的最小数字和

# 先初始化 dp 第一列和第一行的所有值
# 然后利用递推公式：dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
# 求得 dp

# 最后返回 dp[m - 1][n - 1] 即可


class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[grid[0][0]] * n for _ in range(m)]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
