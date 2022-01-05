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
### Method1: 
# 索引左侧所有数字的乘积 * 索引右侧所有数字的乘积（即前缀与后缀）相乘
class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        
        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]

        for i in range(length):
            answer[i] = L[i] * R[i]
       
        return answer

print(Solution().productExceptSelf(nums=[1,2,3,4]))

### Method1 复杂度分析
# 时间复杂度：O(N)，其中 N 指的是数组 nums 的大小
# 预处理 L 和 R 数组以及最后的遍历计算都是 O(N) 的时间复杂度。
# 空间复杂度: O(N)，其中 N 指的是数组 nums 的大小
# 使用了 L 和 R 数组去构造答案，L 和 R 数组的长度为数组 nums 的大小。


### Method2:
# 由于输出数组不算在空间复杂度内，那么我们可以将 L 或 R 数组用输出数组来计算
# 先把输出数组当作 L 数组来计算，然后再动态构造 R 数组得到结果。

class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [0]*length

        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer

### Method2 复杂度分析:
# 时间复杂度：O(N)，其中 N 指的是数组 nums 的大小
# 空间复杂度：O(1)，输出数组不算进空间复杂度中，因此我们只需要常数的空间存放变量

print(Solution().productExceptSelf(nums=[1,2,3,4]))
