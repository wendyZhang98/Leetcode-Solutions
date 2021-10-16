### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0264.Ugly%20Number%20II/README_EN.md


### Description:
# 给你一个整数 n ，请你找出并返回第 n 个丑数
# 丑数 就是只包含质因数 2、3 和/或 5 的正整数



### Example:
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数



### Solution:
# 动态规划法

# 定义数组 dp，
# dp[i - 1] 表示第 i 个丑数，那么第 n 个丑数就是 dp[n - 1]
# 最小的丑数是 1，所以 dp[0] = 1

# 定义 3 个指针 p2，p3，p5，
# 表示下一个丑数是当前指针指向的丑数乘以对应的质因数。
# 初始时，三个指针的值都指向 0。
# 当 i∈[1,n)，dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
# 然后分别比较 dp[i] 与 dp[p2] * 2、dp[p3] * 3、dp[p5] * 5 是否相等
# 若是，则对应的指针加 1。

# 最后返回 dp[n - 1] 即可。



class Solution:
    def nthUglyNumber(self, n):
        dp = [1] * n
        p2 = p3 = p5 = 0
        for i in range(1, n):
            next2, next3, next5 = dp[p2] * 2, dp[p3] * 3, dp[p5] * 5
            dp[i] = min(next2, next3, next5)
            if dp[i] == next2:
                p2 += 1
            if dp[i] == next3:
                p3 += 1
            if dp[i] == next5:
                p5 += 1
        return dp[-1]