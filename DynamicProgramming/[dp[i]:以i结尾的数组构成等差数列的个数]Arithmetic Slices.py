### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0400-0499/0413.Arithmetic%20Slices/README.md



### Description:
# 如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列

# 例如，以下数列为等差数列:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 以下数列不是等差数列。
# 1, 1, 2, 5, 7

# 数组 A 包含 N 个数，且索引从0开始。
# 数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。
# 如果满足以下条件，则称子数组(P, Q)为等差数组：
# 元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P+1<Q 。
# 函数要返回数组 A 中所有为等差数组的子数组个数。



### Example:
# A = [1, 2, 3, 4]
# 返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。



### Solution:
# 动态规划法
# 设 dp[i] 表示以 i 结尾的数组构成的等差数列的个数。
# 如果 nums[i] + nums[i - 2] ≠ nums[i - 1] * 2，
# 说明以 i 结尾的数组无法构成等差数列，dp[i] = 0；
# 否则 dp[i] = 1 + dp[i - 1]。
# 结果返回 dp 数组所有元素之和即可。

class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        dp = [0] * n
        for i in range(2, n):
            if nums[i] + nums[i-2] == nums[i-1] * 2:
                dp[i] = 1 + dp[i-1]
        print(dp)
        return sum(dp)
print(Solution().numberOfArithmeticSlices(nums=[1, 2, 3, 4]))

