### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0016.3Sum%20Closest/README.md


### Description:
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
# 找出 nums 中的三个整数，使得它们的和与 target 最接近。
# 返回这三个数的和。
# 假定每组输入只存在唯一答案。


# 示例：
# 输入：nums = [-1, 2, 1, -4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2(-1 + 2 + 1 = 2)


# 提示：
# 3 <= nums.length <= 10 ^ 3
# -10 ^ 3 <= nums[i] <= 10 ^ 3
# -10 ^ 4 <= target <= 10 ^ 4


### Solution:
# 双指针解决


###
class Solution:
    def threeSumClosest(self, nums, target):
        def twoSumClosest(nums, start, end, target):
            res = 0
            diff = 10000
            while start < end:
                val = nums[start] + nums[end]
                if val == target:
                    return val
                if abs(val - target) < diff:
                    res = val
                    diff = abs(val - target)
                if val < target:
                    start += 1
                else:
                    end -= 1
            return res

        nums.sort()
        res, n = 0, len(nums)
        diff = 10000
        for i in range(n - 2):
            t = twoSumClosest(nums, i + 1, n - 1, target - nums[i])
            if abs(nums[i] + t - target) < diff:
                res = nums[i] + t
                diff = abs(nums[i] + t - target)
        return res