### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0345.Reverse%20Vowels%20of%20a%20String/README_EN.md


# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。


# 输入："hello"
# 输出："holle"


# 输入："leetcode"
# 输出："leotcede"


# 提示：元音字母不包含字母 "y"
# 将字符串转为字符数组（或列表），定义双指针 i、j，分别指向数组（列表）头部和尾部
# 当 i、j 指向的字符均为元音字母时，进行交换。
# 依次遍历，当 i >= j 时，遍历结束。将字符数组（列表）转为字符串返回即可。

class Solution:
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s) - 1
        chars = list(s)
        while i < j:
            if chars[i] not in vowels:
                i += 1
                continue
            if chars[j] not in vowels:
                j -= 1
                continue
            chars[i], chars[j] = chars[j], chars[i]
            i += 1
            j -= 1
        return ''.join(chars)

string_to_be_reversed = 'LeetCode'
string_after_being_reversed = Solution().reverseVowels(string_to_be_reversed)
print(string_after_being_reversed)


