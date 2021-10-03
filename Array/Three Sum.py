### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0015.3Sum/README.md


### Description:
# 给你一个包含 n 个整数的数组 nums，
# 判断 nums 中是否存在三个元素 a, b, c,
# 使得 a + b + c = 0 ？
# 请你找出所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。


### Example
# 示例 1：
# 输入：nums = [-1, 0, 1, 2, -1, -4]
# 输出：[[-1, -1, 2], [-1, 0, 1]]

# 示例 2：
# 输入：nums = []
# 输出：[]

# 示例3：
# 输入：nums = [0]
# 输出：[]

# 提示：
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105


### Solution：
# “排序 + 双指针”实现。


###
class Solution:
    def threeSum(self, nums):
        n, res = len(nums), []

        if n < 3:
            return res

        nums.sort() # ascending
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < n and nums[j] == nums[j - 1]:
                        j += 1
                    while k > i and nums[k] == nums[k + 1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        return res