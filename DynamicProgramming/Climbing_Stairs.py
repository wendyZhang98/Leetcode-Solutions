### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0070.Climbing%20Stairs/README.md
# https://leetcode-cn.com/problems/climbing-stairs/solution/dai-ma-sui-xiang-lu-dong-tai-gui-hua-jin-y1hw/


### Description:
# 假设你正在爬楼梯
# 需要 n 阶你才能到达楼顶
# 每次你可以爬 1 或 2 个台阶
# 你有多少种不同的方法可以爬到楼顶呢

# 注意：给定 n 是一个正整数

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶
# 1.  1 阶 + 1 阶
# 2.  2 阶

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶


### Solution:
# 想上第 n 级台阶，可从第 n-1 级台阶爬一级上去，也可从第 n-2 级台阶爬两级上去，即：f(n) = f(n-1) + f(n-2)；递推求解即可


class Solution:
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n+1):
            for j in range(1, 3):
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[-1]
