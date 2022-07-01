Description:
- https://leetcode.cn/problems/longest-substring-without-repeating-characters/

Example: 
- s = "abcabcbb"
- 3 ("abc")

- s = "bbbbb"
- 1 ("b")

- s = "pwwkew"
- 3 ("wke")


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


