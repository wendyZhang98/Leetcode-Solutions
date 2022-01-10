### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0322.Coin%20Change/README.md



### Description:
# 给定不同面额的硬币 coins 和一个总金额 amount
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数
# 如果没有任何一种硬币组合能组成总金额，返回 -1
# 你可以认为每种硬币的数量是无限的

# 动态规划,类似完全背包的思路
# 硬币数量不限，求凑成总金额所需的最少的硬币个数



### 背包专题：
# https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-dong-tai-gui-hua-e2nt7/



### Example:
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1

# 输入：coins = [2], amount = 3
# 输出：-1

# 输入：coins = [1], amount = 0
# 输出：0

# 输入：coins = [1], amount = 1
# 输出：1

# 输入：coins = [1], amount = 1
# 输出：1


### Solution:
# https://leetcode-cn.com/problems/coin-change/solution/322-ling-qian-dui-huan-by-leetcode-solution/
# 定义 F(i) 为组成金额 i 所需最少的硬币数量
# F(i) 对应的状态转移方程为 F(i) = min_{j=0,...,n-1}F(i-c_j) + 1
# 其中，c_j 代表的是第 j 枚硬币的面值

class Solution:
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 

print(Solution().coinChange(coins=[1, 2, 5], amount=11))
