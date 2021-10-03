### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0045.Jump%20Game%20II/README.md


### Description:
# 给定一个非负整数数组，你最初位于数组的第一个位置
# 数组中的每个元素代表你在该位置可以跳跃的最大长度
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置


### Example:
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。


# 假设你总是可以到达数组的最后一个位置。


# ？？？
# class Solution:
#     def jump(self, nums):
#         end = mx = steps = 0
#         for i, num in enumerate(nums[:-1]):
#             mx = max(mx, i + num)
#             if i == end:
#                 end = mx
#                 steps += 1
#         return steps
#
#
# print(Solution().canJump(nums=[2, 3, 1, 3, 4]))