### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0088.Merge%20Sorted%20Array/README.md



### Description:
# 给你两个有序整数数组 nums1 和 nums2，
# 请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
# 你可以假设 nums1 的空间大小等于 m + n，
# 这样它就有足够的空间保存来自 nums2 的元素。


### Example:
# 示例 1：
# 输入：nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
# 输出：[1, 2, 2, 3, 5, 6]

# 示例 2：
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]

# 提示：
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[i] <= 109


### Solution:
# 双指针解决


###
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything,
        modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1