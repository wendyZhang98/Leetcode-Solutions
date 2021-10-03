### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0283.Move%20Zeroes/README.md


### Description:
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。


### Example:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。


###
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything,
        modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        zero_count = 0
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
            else:
                nums[i - zero_count] = nums[i]
        while zero_count > 0:
            nums[n - zero_count] = 0
            zero_count -= 1