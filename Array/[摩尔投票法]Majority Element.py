### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0169.Majority%20Element/README.md


### Description:
# 给定一个大小为 n 的数组，
# 找到其中的多数元素。
# 多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，
# 并且给定的数组总是存在多数元素。


### Example:
# 示例1：
# 输入：[3, 2, 3]
# 输出：3

# 示例2：
# 输入：[2, 2, 1, 1, 1, 2, 2]
# 输出：2

# 进阶：
# 尝试设计时间复杂度为O(n)、空间复杂度为O(1)的算法解决此问题。


### Solution:
# 摩尔投票法
# 时间复杂度 O(n)，空间复杂度 O(1)
 
# 摩尔投票法（Boyer–Moore majority vote algorithm），也被称作「多数投票法」
# 算法解决的问题是：如何在任意多的候选人中（选票无序），选出获得票数最多的那个。
# 算法可以分为两个阶段：

# 对抗阶段：分属两个候选人的票数进行两两对抗抵消
# 计数阶段：计算对抗结果中最后留下的候选人票数是否有效


class Solution:
    def majorityElement(self, nums):
        cnt = major = 0
        for num in nums:
            if cnt == 0:
                major = num
                cnt = 1
            else:
                cnt += (1 if major == num else -1)
        return major

print(Solution().majorityElement(nums=[4, 4, 4, 3, 3, 4]))
