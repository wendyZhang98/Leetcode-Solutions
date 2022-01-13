### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0300.Longest%20Increasing%20Subsequence/README_EN.md




### Description:
# 给你一个整数数组 nums, 找到其中最长严格递增子序列的长度
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序
# 例如: [3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列

# 进阶：
# 你可以设计时间复杂度为 O(n2) 的解决方案吗？
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?




### Example:
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4

# 输入：nums = [0,1,0,3,2,3]
# 输出：4

# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1




### Solution:
### 动态规划
# 如果 把 f[i] 定义为 0～i 所有数字能组成的 严格递增子序列 的最大长度，会发现不太好做
# 但是如果把 f[i] 定义为 以 nums[i] 结尾的 所有 严格递增子序列 的最大长度就可以了！

# 定义 dp[i] 为以 nums[i] 结尾的最长子序列的长度，dp[i] 初始化为 1 (i∈[0, n))
# 即题目求的是 dp[i] （i ∈[0, n-1]）的最大值

# 状态转移方程为：
# dp[i] = max(dp[j]) + 1
# 其中 0≤j<i 且 nums[j]<nums[i]

class Solution:
  def lengthOfLIS(self, nums):
    n = len(nums)
    dp = [1] * n    # dp[i]: 以 nums[i] 结尾的所有严格递增子序列的最大长度
      
    for i in range(n):
      for j in range(i):
        if nums[j] < nums[i]:   # 如果 nums[i] 大于之前的一个 nums[j]，那么 nums[i] 可以拼在其后 延长严格递增子序列
          dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

Solution().lengthOfLIS(nums=[10,9,2,5,3,7,101,18])
