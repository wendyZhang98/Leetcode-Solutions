### Description:
- https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0088.Merge%20Sorted%20Array/README.md



### Description:
- 给你两个有序整数数组 nums1 和 nums2，
- 请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
- 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
- 你可以假设 nums1 的空间大小等于 m + n，
- 这样它就有足够的空间保存来自 nums2 的元素。


### Example:
#1: 
- Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
- Output: [1, 2, 2, 3, 5, 6]

#2: 
- Input: nums1 = [1], m = 1, nums2 = [], n = 0
- Output: [1]


### Solution:
```
class Solution:
    def merge(self, nums1, m, nums2, n):

        i, j, k = m - 1, n - 1, m + n - 1
        nums1 = nums1 + [0] * n
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        return nums1

print(Solution().merge(nums1=[1,3,5], m=3, nums2=[2,4,6], n=3))
print(Solution().merge(nums1=[1,5,7], m=3, nums2=[2,4,6], n=3))
```
