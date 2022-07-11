### Descriptions:
- https://leetcode.com/problems/reverse-only-letters/


### Examples:
<img width="601" alt="Screen Shot 2022-02-25 at 11 55 44" src="https://user-images.githubusercontent.com/49216429/155755487-e08ff340-932c-4056-a4b9-4f884dc3d182.png">

### Solutions:
<img width="628" alt="Screen Shot 2022-02-25 at 12 08 54" src="https://user-images.githubusercontent.com/49216429/155757339-697a0d9d-7f79-4f34-b440-b7cb08507196.png">

```
class Solution(object):
    def reverseOnlyLetters(self, S):
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        
        return "".join(ans)
```

### Complexity Analysis:
<img width="616" alt="Screen Shot 2022-02-25 at 12 09 34" src="https://user-images.githubusercontent.com/49216429/155757446-2112eaf0-629f-49cf-82e1-b441b8ccc63c.png">
