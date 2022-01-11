### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0343.Integer%20Break/README.md




### Description:
# 给定一个正整数 n, 将其拆分为至少两个正整数的和
# 并使这些整数的乘积最大化; 返回你可以获得的最大乘积




### Example:
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1

# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36




### Solution:
# https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/

# 动态规划
# dp[i] 表示正整数 i 能获得的最大乘积
# 初始化 dp[0] = dp[1] = 1

# i >= 2 时
# 假设正整数 i 拆分出的第一个正整数是 j
# 将 i 拆分成 j 和 i - j 的和后，则有两种方案
# 1：i-j 不再拆分为多个正整数，此时乘积为 j * (i-j)
# 2：i-j 继续拆分为多个正整数，此时乘积为 j * d[i-j]

# dp[i] = max(j×(i−j), j×dp[i−j]), j∈[1, i-1]
# 需要遍历所有 j 得到 dp[i] 的最大值

class Solution:
    def integerBreak(self, n):
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

print(Solution().integerBreak(n=10))
