### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0500-0599/0518.Coin%20Change%202/README.md


### Description:
# 给定不同面额的硬币和一个总金额
# 写出函数来计算可以凑成总金额的硬币组合数
# 假设每一种面额的硬币有无限个

# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# 动态规划
# 完全背包问题


class Solution:
    def change(self, amount, coins):
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]


print(Solution().change(amount=5, coins=[1, 2, 5]))