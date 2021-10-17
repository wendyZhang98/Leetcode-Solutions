### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0700-0799/0740.Delete%20and%20Earn/README_EN.md


### Description:
# 给定一个整数数组 nums，你可以对它进行一些操作
# 每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数
# 之后，你必须删除每个等于 nums[i]-1 或 nums[i]+1 的元素
# 开始你拥有 0 个点数
# 返回你能通过这些操作获得的最大点数


### Example:
# 输入: nums = [3, 4, 2]
# 输出: 6
# 解释:
# 删除 4 来获得 4 个点数，因此 3 也被删除
# 之后，删除 2 来获得 2 个点数。总共获得 6 个点数

# 输入: nums = [2, 2, 3, 3, 3, 4]
# 输出: 9
# 解释:
# 删除 3 来获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。


### Solution：
# 核心思路: 一个数字要么不选，要么全选
# 首先计算出每个数字的总和 sums，并维护两个 dp 数组：select 和 nonSelect

# sums[i] 代表值为 i 的元素总和
# select[i] 代表如果选数字 i，从 0 处理到 i 的最大和
# nonSelect[i] 代表如果不选数字 i，从 0 处理到 i 的最大和

# 那么我们有以下逻辑：
# 如果选 i，那么 i-1 肯定不能选
# 如果不选 i，那么 i-1 选不选都可以，因此我们选择其中较大的选法
# select[i] = nonSelect[i-1] + sums[i];
# nonSelect[i] = Math.max(select[i-1], nonSelect[i-1]) = Math.max(nonSelect[i-2] + sums[i-1], nonSelect[i-1])


class Solution:
    def deleteAndEarn(self, nums):
        mx = float('-inf')
        for num in nums:
            mx = max(mx, num)
        total = [0] * (mx + 1)
        for num in nums:
            total[num] += num
        first = total[0]
        second = max(total[0], total[1])
        for i in range(2, mx + 1):
            cur = max(first + total[i], second)  # cur: maxAt_i = max(maxAt_[i-2] + Sums[i], maxAt_[i-1])
            first = second                       # first: maxAt_(i-2)
            second = cur                         # second: maxAt_(i-1)
        return second


print(Solution().deleteAndEarn(nums=[2, 2, 3, 3, 3, 4]))
