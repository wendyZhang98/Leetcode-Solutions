# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/




### Description:
# Given an integer array arr and an integer difference
# return the length of the longest subsequence in arr which is an arithmetic sequence 
# such that the difference between adjacent elements in the subsequence equals difference.

# A subsequence is a sequence that can be derived from arr 
# by deleting some or no elements without changing the order of the remaining elements.




### Example:
# Example 1:
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].

# Example 2:
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.

# Example 3:
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].



### Solution:
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/discuss/398216/Python-4-lines

# dp[num]: 以 num 结尾的 最长等差子序列

# method1:
def longestSubsequence(self, arr, diff):
        res = {}
        for num in arr:
            res[num] = res[num-diff] + 1 if (num - diff) in res else 1  # res[num] = res.get(num-diff, 0) + 1
        return max(res.values())

 
# method2:  
import collections
class Solution:
    def longestSubsequence(self, arr, difference):
        dp = collections.defaultdict(int)
        for num in arr:
            dp[num] = max(dp[num], 1+dp[num-difference])
        return max(dp.values())
      
print(Solution().longestSubsequence(arr=[1,5,7,8,5,3,4,2,1], difference=-2))
