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
# 双指针解决


# Method 1
class Solution:
    def threeSumSmaller(self, nums, target):
        size = len(nums)
        ans = 0

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if nums[i] + nums[j] + nums[k] < target:
                        ans += 1
        return ans

print(Solution().threeSumSmaller(nums=[-2, 0, 1, 3], target=2))
# time complexity: O(N3)
# space complexity: O(1)


# Method 2
class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        size = len(nums)

        ans = 0

        for i in range(size - 2):
            l, r = i + 1, size - 1
            aim = target - nums[i]
            while l < r:
                if nums[l] + nums[r] >= aim:
                    r -= 1
                else:
                    ans += r - l
                    l += 1

        return ans

print(Solution().threeSumSmaller(nums=[-2, 0, 1, 3], target=2))
print(Solution().threeSumSmaller(nums=[-2, 0, 1, 3], target=1))
# time complexity: O(N2)
# space complexity: O(N)
