# https://leetcode.com/problems/word-break/



### Description:
# Given a string s and a dictionary of strings wordDict
# return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.




### Examples:
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false




### Solution:
# https://leetcode.com/problems/word-break/solution/

# The intuition behind this approach is that the given problem (s) can be divided into subproblems s1 and s2. 

# If these subproblems individually satisfy the required conditions, the complete problem, s also satisfies the same. 

# e.g. "catsanddog" can be split into two substrings "catsand", "dog". 
# The subproblem "catsand" can be further divided into "cats", "and", 
# which individually are a part of the dictionary making "catsand" satisfy the condition. 
# Going further backwards, "catsand", "dog" also satisfy the required criteria individually 
# leading to the complete string "catsanddog" also to satisfy the criteria.

# Here we use two pointers i and j
# where i refers to the length of the string of the substring s' considered currently starting from the begining
# j refers to the index partitioning the current substring s' into smaller substring s'(0,j) and s'(j+1,i)

# To fill in the dp array, we initialize the element dp[0] as ture
# since the null string is always present in the dictionary
# and the rest of the dp as false 


class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
      
print(Solution().wordBreak(s="catsandog", wordDict=["cats","dog","sand","and","cat"]))


# Time Complexity: O(n**3);  There are two nested loops, and substring computation at each iteration. 
# Space Complexity: O(n); length of p is n+1.
