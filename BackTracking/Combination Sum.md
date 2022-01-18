https://leetcode.com/problems/combination-sum/



### Description
- Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
- You may return the combinations in any order.
- The same number may be chosen from candidates an unlimited number of times. 
- Two combinations are unique if the frequency of at least one of the chosen numbers is different.
- It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



### Examples
| Input | Output | 
| --- | --- |
|candidates = [2,3,6,7], target = 7| [[2,2,3],[7]]|
| candidates = [2,3,5], target = 8 | [[2,2,2,2],[2,3,3],[3,5]] |
|candidates = [2], target = 1 | [] |



### Solutions:
https://leetcode.com/problems/combination-sum/solution/

- This is one of the problems in the series of combination sum. They all can be solved with the same algorithm, i.e. backtracking.

- Before tackling this problem, we would recommend one to start with another almost identical problem called Combination Sum III, which is arguably easier and one can tweak the solution a bit to solve this problem.

- For the sake of this article, we will present the backtracking algorithm. Furthermore, we will list some other problems on LeetCode that one can solve with the same algorithm presented here.


### BackTracking:
- As a reminder, backtracking is a general algorithm for finding all (or some) solutions to some computational problems. 
- The idea is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack") as soon as it determines that this candidate cannot lead to a final solution.

<img width="1172" alt="Screen Shot 2022-01-16 at 17 42 09" src="https://user-images.githubusercontent.com/49216429/149681071-159c9053-c04e-4e2b-bcfb-ae0005a74b45.png">

- An important detail on choosing the next number for the combination is that we select the candidates in order, where the total candidates are treated as a list.
- Once a candidate is added into the current combination, we will not look back to all the previous candidates in the next explorations.

<img width="978" alt="Screen Shot 2022-01-16 at 18 32 08" src="https://user-images.githubusercontent.com/49216429/149682665-2fbb28d3-8508-4d74-b2bc-9d947d3e090f.png">

```
class Solution:
    def combinationSum(self, candidates, target):

        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results
```
