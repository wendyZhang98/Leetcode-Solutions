### Link:
# https://github.com/doocs/leetcode/blob/main/solution/1100-1199/1143.Longest%20Common%20Subsequence/README.md



### Description:
# 给定两个字符串 text1 和 text2
# 返回这两个字符串的最长 公共子序列 的长度
# 如果不存在 公共子序列 ，返回 0

# 一个字符串的 子序列 是指这样一个新的字符串：
# 它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列



### Example_1:
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3

# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3

# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0



### Solution:
# 最长公共子序列问题是典型的二维动态规划问题
# 假设字符串 text1 和 text2 的长度分别为 m 和 n
# 创建 m+1 行 n+1 列的二维数组 dp
# 其中 dp[i][j] 表示 text[0:i] 和 text[0:j] 的最长公共子序列长度

# 考虑动态规划的边界情况 
# 当 i=0, text[0:i] 为空，空字符串和任意字符串 最长公共子序列 长度为0
# 因此对任意 j, dp[0][j]=0
# 同理对任意 i, dp[i][0]=0

# 当 i>0; j>0 时，考虑 dp[i][j]计算：
# 当 text1[i-1] = text2[j-1]: dp[i][j] = dp[i-1][j-1]+1
# 当 text1[i-1] != text2[j-1]: dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

print(Solution().longestCommonSubsequence(text1='ILoveYou', text2='iloveyou'))
