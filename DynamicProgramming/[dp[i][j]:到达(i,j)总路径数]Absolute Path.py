### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0062.Unique%20Paths/README.md


### Description:
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）
# 机器人每次只能向下或者向右移动一步
# 机器人试图达到网格的右下角（在下图中标记为 “Finish” ）
# 问总共有多少条不同的路径？


### Example:
# 输入：m = 3, n = 7
# 输出：28

# 输入：m = 3, n = 2
# 输出：3
# 解释：
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向下

# 输入：m = 7, n = 3
# 输出：28

# 输入：m = 3, n = 3
# 输出：6


### Solution:
# 动态规划
# 假设 dp[i][j] 表示到达网格 (i,j) 的路径数
# 则 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

class Solution:
    def uniquePaths(self, m, n):
        # m:row; n:column
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

print(Solution().uniquePaths(m=7, n=3))
