### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0500-0599/0518.Coin%20Change%202/README.md



### Description:
# 给定不同面额的硬币和一个总金额
# 写出函数来计算可以凑成总金额的硬币组合数
# 假设每一种面额的硬币有无限个



### Example:
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1



### Solution:
# https://leetcode-cn.com/problems/coin-change-2/solution/ling-qian-dui-huan-ii-by-leetcode-soluti-f7uh/

# 动态规划(完全背包问题)
# 给定总金额 amount 和数组 coins，要求计算金额之和等于 amount 的硬币组合数
# 其中，coins 的每个元素可以选取多次，且不考虑选取元素的顺序
# 因此，本题需要计算的是选取硬币的组合数。

# 初始化 dp[0]=1
# 遍历 coins，对于其中每个元素 coin：
# 遍历 i 从 coin 到 amount，将 dp[i-coin] 的值添加到 dp[i]
# 最终得到 dp[amount]的值即是答案

class Solution:
    def change(self, amount, coins):
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] += dp[j-coin]
        return dp[amount]


print(Solution().change(amount=5, coins=[1, 2, 5]))
