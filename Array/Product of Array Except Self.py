### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0238.Product%20of%20Array%20Except%20Self/README.md



### Description:
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output
# 其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积

# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。



### Example:
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]



### Solution:
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1 for _ in nums]
        left = right = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output

print(Solution().productExceptSelf(nums=[1,2,3,4]))
