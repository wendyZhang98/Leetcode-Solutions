### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0198.House%20Robber/README_EN.md


### Description:
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金
# 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警
# 给定一个代表每个房屋存放金额的非负整数数组
# 计算你不触动警报装置的情况下，一夜之内能够偷窃到的最高金额

# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)
#      偷窃到的最高金额 = 1 + 3 = 4

# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)
#      偷窃到的最高金额 = 2 + 9 + 1 = 12


### Solution:
# 动态规划法
# 状态转移方程：f(n) = Math.max(f(n - 2) + nums[n], f(n - 1))


class Solution:
    def rob(self, nums):
        def robRange(nums, start, end):
            if end - start == 0:
                return nums[start]
            pre, cur = 0, nums[start]
            for i in range(start + 1, end + 1):
                pre, cur = cur, max(pre + nums[i], cur)
            return cur
        if not nums:
            return 0
        return robRange(nums, 0, len(nums) - 1)


# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         a, b = 0, nums[0]
#         for num in nums[1:]:
#             a, b = b, max(num + a, b)
#         return b

