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

### Method1:
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

### Complexity Analysis
<img width="775" alt="Screen Shot 2022-06-30 at 23 46 22" src="https://user-images.githubusercontent.com/49216429/176819506-ace724c6-1e57-4a43-8058-61b8be8b2974.png">

### Method2: 
<img width="783" alt="Screen Shot 2022-06-30 at 23 48 23" src="https://user-images.githubusercontent.com/49216429/176819687-52a2c94e-1279-4924-8f15-c443f1719b1b.png">

```
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
        
        return strs[0]
```

### Complexity Analysis:
<img width="768" alt="Screen Shot 2022-06-30 at 23 51 32" src="https://user-images.githubusercontent.com/49216429/176820000-37ec5c93-672a-4355-8ffa-95f3c54c8408.png">

### Method3: 
<img width="787" alt="Screen Shot 2022-07-01 at 11 42 00" src="https://user-images.githubusercontent.com/49216429/176926884-59537db5-a668-4cd9-a62e-60ec99b8b819.png">

```
class Solution:
    def longestCommonPrefix(self, strs):
        def lcp(start, end):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]

            return lcpLeft[:minLength]

        return "" if not strs else lcp(0, len(strs) - 1)
```

### Complexity Analysis:
<img width="769" alt="Screen Shot 2022-07-01 at 11 43 27" src="https://user-images.githubusercontent.com/49216429/176927108-2072e2db-b00b-417f-a761-c6427f46fcdb.png">

### Method4:
<img width="790" alt="Screen Shot 2022-07-01 at 12 11 38" src="https://user-images.githubusercontent.com/49216429/176931561-2b9420f8-71a9-43d0-95a1-cf4640647e84.png">

```
class Solution:
    def longestCommonPrefix(self, strs):
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]
```

### Complexity Analysis:
<img width="771" alt="Screen Shot 2022-07-01 at 12 15 49" src="https://user-images.githubusercontent.com/49216429/176932160-19492c95-227c-4a9d-9cb0-c39ac9ab6a66.png">


