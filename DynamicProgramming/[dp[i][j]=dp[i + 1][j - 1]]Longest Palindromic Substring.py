### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0005.Longest%20Palindromic%20Substring/README.md



### Description:
# 给你一个字符串 s，找到 s 中最长的回文子串



### Example:
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。

# 输入：s = "cbbd"
# 输出："bb"

# 输入：s = "a"
# 输出："a"

# 输入：s = "ac"
# 输出："a"



### Solution:
# 动态规划法
# 对于一个 子串 而言， 如果它是回文串， 并且长度大于 2
# 那么将其 首尾 两个字母去除之后，它仍然是个 回文串
# 例如 “ababa“，如果我们已经知道 “bab” 是回文串，那么 “ababa” 一定是回文串
# 根据此思路：
# 设 dp[i][j] 表示字符串 s[i..j] 是否为回文串: true or false 
# 当 j - i < 3，即字符串长度为 3 时，只要 s[i] == s[j]，dp[i][j] 就为 true
# 当 j - i > 3，dp[i][j] = dp[i + 1][j - 1] && s[i] == s[j]




# https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/

class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n < 2:
            return s
        
        max_len = 1
        begin = 0
       
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
 
        for L in range(2, n + 1):  # 枚举 子串长度
            for i in range(n):     # 枚举 左边界
                j = L + i - 1      # 右边界 可由 L 和 i 共同确定
                if j >= n:         # 如果 右边界 越界；退出当前循环
                    break

                if s[i] != s[j]:   
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
                    
        return s[begin : begin + max_len]

print(Solution().longestPalindrome(s="sabbaa"))
