https://leetcode.com/problems/generate-parentheses/



### Description:
- Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



### Examples:
|Input|Output|
|---|---|
|n = 3|["((()))","(()())","(())()","()(())","()()()"]|
|n = 1|["()"]|



### Solutions:
<img width="1249" alt="Screen Shot 2022-01-18 at 00 10 39" src="https://user-images.githubusercontent.com/49216429/149874534-4ff9b599-c551-4eda-aaf2-c2184ad9abc9.png">

```
class Solution(object):
    def generateParenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans
```

<img width="1214" alt="Screen Shot 2022-01-18 at 00 11 22" src="https://user-images.githubusercontent.com/49216429/149874601-0b497e9c-e225-4c2d-b8e6-87af95efeb72.png">

```
class Solution:
    def generateParenthesis(self, n):
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans
```
