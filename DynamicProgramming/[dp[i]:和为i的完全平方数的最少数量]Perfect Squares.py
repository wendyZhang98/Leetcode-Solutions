### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0279.Perfect%20Squares/README.md




### Description:
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n
# 你需要让组成和的完全平方数的个数最少

# 给你一个整数 n ，返回和为 n 的完全平方数的 最少数量
# 完全平方数 是一个整数，其值等于另一个整数的平方

# 换句话说，其值等于一个整数自乘的积
# 例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是




### Example:
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4

# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9




### Solution:
# https://leetcode-cn.com/problems/perfect-squares/solution/python3-dong-tai-gui-hua-by-caiji-ud-bnip/

# 动态规划
# 状态定义：dp[i] 表示 i 的完全平方数的最少数量
# 状态转移：遍历1...i内的平方数 j*j，j由1开始递增
# dp[i] = min(dp[i], dp[i-j*j]+1)
# 边界情况：dp[i] = i


class Solution:
    def numSquares(self, n):
        dp = list(range(n+1))
        for i in range(1, n+1):
            j = 1
            while i - j*j>=0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[-1]
    
print(Solution().numSquares(n=10)) # 1+3**2
