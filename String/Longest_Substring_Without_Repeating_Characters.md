### Description:
- https://leetcode.cn/problems/longest-substring-without-repeating-characters/

### Examples:
#1: 
- input: s = "abcabcbb"
- output: 3 ("abc")

#2:
- input: s = "bbbbb"
- output: 1 ("b")

#3:
- input: s = "pwwkew"
- output: 3 ("wke")

### Solution
- https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/

<img width="705" alt="Screen Shot 2022-06-30 at 22 24 06" src="https://user-images.githubusercontent.com/49216429/176811043-138364ed-85aa-4320-a302-cd6dfe86a1ee.png">

```
class Solution:
    def lengthOfLongestSubstring(self, s):
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans
```

### Complexity Analysis
<img width="762" alt="Screen Shot 2022-06-30 at 23 22 41" src="https://user-images.githubusercontent.com/49216429/176817206-95da0f3f-4d95-4554-9669-9c8ec55c2604.png">
