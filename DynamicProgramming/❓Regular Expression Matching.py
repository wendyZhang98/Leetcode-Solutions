# https://leetcode.com/problems/regular-expression-matching/



### Description:
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

# '.' Matches any single character. 
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).



### Examples:
# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input: s = "ab", p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Example 4:
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

# Example 5
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false



### Solution:
# https://leetcode.com/problems/regular-expression-matching/solution/


### Approach1: Recursion
# Intuition: 
# If there were no Kleene stars (the * wildcard character for regular expressions), 
# the problem would be easier - we simply check from left to right if each character of the text matches the pattern.
# When a star is present, we may need to check many different suffixes of the text 
# and see if they match the rest of the pattern. 
# A recursive solution is a straightforward way to represent this relationship.

def match(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])
  
# If a star is present in the pattern, it will be in the second position pattern[1]. 
# Then, we may ignore this part of the pattern, or delete a matching character in the text. 
# If we have a match on the remaining strings after any of these operations, then the initial inputs matched.

class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or (first_match and self.isMatch(text[1:], pattern)))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

        
### Approach2: DP

# As the problem has an optimal substructure, it is natural to cache intermediate results. We ask the question dp(i, j): 
# does text[i:] and pattern[j:] match? We can describe our answer in terms of answers to questions involving smaller strings.

### Top-Down Variation

class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)
     
### Bottom-Up Variation

class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]
