### Description:
- https://leetcode.cn/problems/reverse-vowels-of-a-string/


### Examples:
#1 
- input: s="hello"
- output: "holle"

#2 
- input: s="leetcode"
- output: s='leotcede"


### Solutions:
- https://leetcode.cn/problems/reverse-vowels-of-a-string/solution/fan-zhuan-zi-fu-chuan-zhong-de-yuan-yin-2bmos/
<img width="777" alt="Screen Shot 2022-07-01 at 12 27 03" src="https://user-images.githubusercontent.com/49216429/176933936-2d159b6f-ce1b-4b32-b36a-681ce9dcd146.png">

```
class Solution:
    def reverseVowels(self, s):
        def isVowel(ch):
            return ch in "aeiouAEIOU"
        
        n = len(s)
        s = list(s)
        i, j = 0, n - 1
        while i < j:
            while i < n and not isVowel(s[i]):
                i += 1
            while j > 0 and not isVowel(s[j]):
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)
```

### Complexity Analysis:
<img width="762" alt="Screen Shot 2022-07-01 at 12 29 12" src="https://user-images.githubusercontent.com/49216429/176934246-274bc355-18dc-4460-8d10-e2032186ed0f.png">

