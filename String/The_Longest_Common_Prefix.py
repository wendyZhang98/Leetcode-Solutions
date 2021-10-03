### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0014.Longest%20Common%20Prefix/README.md


# 编写一个函数来查找字符串数组中的最长公共前缀
# 如果不存在公共前缀，返回空字符串 ""

# 输入：strs = ["flower","flow","flight"]
# 输出："fl"

# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。


class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ''
        for i in range(len(strs[0])):
            for j in range(1, n):
                if len(strs[j]) <= i or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


