- https://leetcode.com/problems/combination-sum-iii/



### Description:
- Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
- Only numbers 1 through 9 are used. Each number is used at most once. Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 
 
### Examples:
|Input|Output|
|---|---|
|k = 3, n = 7|[[1,2,4]]|
|k = 3, n = 9|[[1,2,6],[1,3,5],[2,3,4]]|
|k = 4, n = 1|[]|



### Solution:
https://leetcode.com/problems/combination-sum-iii/solution/

- The problem asks us to come up with some fixed-length combinations that meet certain conditions.
- To solve the problem, it would be beneficial to build a combination by hand. If we represent the combination as an array, we then could fill the array one element at a time.
- For example, given the input k=3 and n=9, i.e. the size of the combination is 3, and the sum of the digits in the combination should be 9. Here are a few steps that we could do:

<img width="825" alt="Screen Shot 2022-01-16 at 19 02 37" src="https://user-images.githubusercontent.com/49216429/149683526-f3ad58ad-9153-4a88-9648-bfc840cd7846.png">


- The trick is that we pick the candidates in order. We treat the candidate digits as a list with order, i.e. [1, 2, 3, 4, 5, 6, 7, 8. 9]. At any given step, once we pick a digit, e.g. 6, we will not consider any digits before the chosen digit for the following steps, e.g. the candidates are reduced down to [7, 8, 9].
- With the above strategy, we could ensure that a digit will never be picked twice for the same combination. Also, all the combinations that we come up with would be unique.



```
class Solution:
    def combinationSum3(self, k, n):
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
