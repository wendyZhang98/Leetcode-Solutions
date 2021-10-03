# Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0154.Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II/README.md



### Description:
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。

# 例如，原数组 nums = [0,1,4,4,5,6,7]
# 在变化后可能得到：
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
# 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]

# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为
# 数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]]

# 给你一个可能存在 重复 元素值的数组 nums，它原来是一个升序排列的数组，
# 并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素



### Example:
# 示例 1：
# 输入：nums = [1,3,5]
# 输出：1

# 示例 2：
# 输入：nums = [2,2,2,0,1]
# 输出：0



### Solution:
# 二分法
# 若 nums[m] > nums[r]，说明最小值在 m 的右边；
# 若 nums[m] < nums[r]，说明最小值在 m 的左边（包括 m);
# 若相等，无法判断，直接将 r 减 1。
# 循环比较
# 最后返回 nums[l] 即可。



###
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
        return nums[l]


