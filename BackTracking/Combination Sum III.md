- https://leetcode.com/problems/combination-sum-iii/



### Description:
- Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

- Only numbers 1 through 9 are used.
- Each number is used at most once.
- Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 
 
### Examples:
|Input|Output|
|---|---|
|k = 3, n = 7|[[1,2,4]]|
|k = 3, n = 9|[[1,2,6],[1,3,5],[2,3,4]]|
|k = 4, n = 1|[]|



### Solution:


```
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results
```
