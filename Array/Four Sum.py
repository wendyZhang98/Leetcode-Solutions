### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0018.4Sum/README.md



### Description:
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，
# 判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
# 找出所有满足条件且不重复的四元组。
# 注意：答案中不可以包含重复的四元组。



### Example:
# 示例 1：
# 输入：nums = [1, 0, -1, 0, -2, 2], target = 0
# 输出：[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
#
# 示例 2：
# 输入：nums = [], target = 0
# 输出：[]
#
# 提示：
# 0 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109


### Solution：
# 解法：“排序 + 双指针”实现。



###
class Solution:
    def fourSum(self, nums, target):
        n, res = len(nums), []
        if n < 4:
            return []
        nums.sort()
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < n and nums[k] == nums[k - 1]:
                            k += 1
                        while l > j and nums[l] == nums[l + 1]:
                            l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1
        return res