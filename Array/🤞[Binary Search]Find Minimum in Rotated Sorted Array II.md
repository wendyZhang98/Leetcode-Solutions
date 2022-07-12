### Description:
- https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0154.Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II/README.md

- 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转后，得到输入数组。
- 数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为 [a[n-1], a[0], a[1], a[2], ..., a[n-2]]
- 给你一个可能存在重复元素值的数组 nums，它原来是一个升序排列的数组，
- 并按上述情形进行了多次旋转。请你找出并返回数组中的最小元素



### Examples:
#1
- Input: nums = [1,3,5]
- Output: 1

#2
- Input: nums = [2,2,2,0,1]
- Output: 0



### Solution:
- 若 nums[m] > nums[r]，说明最小值在 m 的右边
- 若 nums[m] < nums[r]，说明最小值在 m 的左边（包括 m)
- 若相等，无法判断，直接将 r 减 1
- 循环比较
- 最后返回 nums[l] 即可

```
class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
        return nums[l]


print(Solution().findMin(nums=[2,2,2,0,1]))
print(Solution().findMin(nums=[5,7,9,1,3,4]))
```
