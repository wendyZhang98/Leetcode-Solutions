### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0259.3Sum%20Smaller/README.md


### Description:
# 给定一个长度为 n 的整数数组和一个目标值 target，
# 寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组
# i, j, k 个数（0 <= i < j < k < n）


### Example:
# 示例 1:
# 输入: nums = [-2,0,1,3], target = 2
# 输出: 2
# 解释: 因为一共有两个三元组满足累加和小于 2:
#      [-2,0,1]
#      [-2,0,3]


# 进阶：是否能在 O(n2) 的时间复杂度内解决？


### Solution:
双指针解决


###
class Solution:
    def threeSumSmaller(self, nums, target):
        def threeSumSmaller(nums, start, end, target):
            count = 0
            while start < end:
                if nums[start] + nums[end] < target:
                    count += (end - start)
                    start += 1
                else:
                    end -= 1
            return count

        nums.sort()
        n, count = len(nums), 0
        for i in range(n - 2):
            count += threeSumSmaller(nums, i + 1, n - 1, target - nums[i])
        return count
