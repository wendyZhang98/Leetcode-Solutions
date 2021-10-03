### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0213.House%20Robber%20II/README.md


### Description:
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
# 这个地方所有的房屋都围成一圈
# 这意味着第一个房屋和最后一个房屋是紧挨着的
# 同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额

# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。

# 输入：nums = [0]
# 输出：0

### Solution:
# 环状排列意味着第一个房屋和最后一个房屋中最多只能选择一个偷窃
# 因此可以把此环状排列房间问题约化为两个单排排列房屋子问题


class Solution:
    def rob(self, nums):
        def robRange(nums, l, r):
            a, b = 0, nums[l]
            for num in nums[l + 1: r + 1]:
                a, b = b, max(num + a, b)
            return b

        n = len(nums)
        if n == 1:
            return nums[0]
        s1, s2 = robRange(nums, 0, n - 2), robRange(nums, 1, n - 1)
        return max(s1, s2)


### Test
print(Solution().rob(nums=[2,3,2]))
print(Solution().rob(nums=[1,2,3,1]))
