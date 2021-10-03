### Link：
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0003.Longest%20Substring%20Without%20Repeating%20Characters/README.md
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/

### 滑动窗口
### HashMap

class Solution:
    def lengthOfLongestSubstring(self, s):
        # HashMap, to check whether each element has appeared
        occ = set()
        n = len(s)
        # rk: the right pointer, initial = -1 (before we make any move)
        rk, ans = -1, 0
        # i: the left pointer, initial = 0 (before we make any move)
        for i in range(n):
            if i != 0:
                # move forward the left pointer
                # delete the string
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # move forward the right pointer
                occ.add(s[rk + 1])
                rk += 1
            # from rk to i, is the longest un-repeated string util now
            ans = max(ans, rk - i + 1)
        return ans


