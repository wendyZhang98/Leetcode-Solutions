### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0042.Trapping%20Rain%20Water/README.md


### Description:
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

# 输入：height = [4,2,0,3,2,5]
# 输出：9


### Solution:
# 动态规划法
# 对于下标 i，水能达到的最大高度等于下标 i 左右两侧的最大高度的最小值，再减去 height[i] 就能得到当前柱子所能存的水量。


class Solution:
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0

        left_max = [height[0]] * n
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [height[n - 1]] * n
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res
