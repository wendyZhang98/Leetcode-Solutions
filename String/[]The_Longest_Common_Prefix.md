### Description：
- https://leetcode.cn/problems/longest-common-prefix/


### Examples:
#1
- input: strs = ["flower","flow","flight"]
- output: "fl"

#2
- input: strs = ["dog","racecar","car"]
- output: ""


### Solutions:
- https://leetcode.cn/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/

<img width="800" alt="Screen Shot 2022-06-30 at 23 43 16" src="https://user-images.githubusercontent.com/49216429/176819182-b10be7e9-1179-465f-ae33-2f62d6a28b32.png">

```
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
```


