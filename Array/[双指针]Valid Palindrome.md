### Descriptions:
https://leetcode.com/problems/valid-palindrome/
<img width="629" alt="Screen Shot 2022-02-25 at 11 27 26" src="https://user-images.githubusercontent.com/49216429/155751064-03c7fd06-cc44-42bb-88aa-4c7050379ff5.png">


### Examples:
<img width="619" alt="Screen Shot 2022-02-25 at 11 27 39" src="https://user-images.githubusercontent.com/49216429/155751091-d67a7def-a04a-4e37-abda-72cbed4f2f23.png">
<img width="617" alt="Screen Shot 2022-02-25 at 11 33 05" src="https://user-images.githubusercontent.com/49216429/155751908-8c354d97-b3c7-4182-8f94-e99ed83d4478.png">
<img width="571" alt="Screen Shot 2022-02-25 at 11 33 29" src="https://user-images.githubusercontent.com/49216429/155751969-f20b2d59-dfcf-443c-a5d9-57467c22154f.png">
<img width="502" alt="Screen Shot 2022-02-25 at 11 33 37" src="https://user-images.githubusercontent.com/49216429/155751998-5138e9a5-aea2-446a-8ecd-e44993eecf7a.png">
<img width="533" alt="Screen Shot 2022-02-25 at 11 33 48" src="https://user-images.githubusercontent.com/49216429/155752037-d7e51d4a-09da-4a9f-9003-a7b75cbed1ad.png">
<img width="605" alt="Screen Shot 2022-02-25 at 11 40 53" src="https://user-images.githubusercontent.com/49216429/155753112-38bc1eee-ecfe-4ff2-b26f-9f3ba36cc724.png">

```
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
```

### Complexity Analysis:
<img width="620" alt="Screen Shot 2022-02-25 at 11 49 06" src="https://user-images.githubusercontent.com/49216429/155754411-b574f7e4-5223-471c-a8b0-c6660da143d3.png">
