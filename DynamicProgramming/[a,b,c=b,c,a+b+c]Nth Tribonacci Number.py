### Link:
# https://github.com/doocs/leetcode/blob/main/solution/1100-1199/1137.N-th%20Tribonacci%20Number/README.md


### Description:
# 泰波那契序列 Tn 定义如下：
# T0 = 0, T1 = 1, T2 = 1
# 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值


### Example
# 输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# 输入：n = 25
# 输出：1389537


class Solution:
    def tribonacci(self, n):
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a+b+c
        return a


print(Solution().tribonacci(n=25))
