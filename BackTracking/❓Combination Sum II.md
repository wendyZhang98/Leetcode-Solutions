- https://leetcode.com/problems/combination-sum-ii/




### Description:
- Given a collection of candidate numbers (candidates) and a target number (target), 
- find all unique combinations in candidates where the candidate numbers sum to target.
- Each number in candidates may only be used once in the combination.
- Note: The solution set must not contain duplicate combinations.

 
 
 
### Examples:
|Input|Output|
|---|---|
|candidates = [10,1,2,7,6,1,5], target = 8|[[1,1,6],[1,2,5],[1,7],[2,6]]|
|candidates = [2,5,2,1,2], target = 5|[[1,2,2],[5]]|



### Solution:

- Approach1: BackTracking with Counters

<img width="1275" alt="Screen Shot 2022-01-17 at 00 05 21" src="https://user-images.githubusercontent.com/49216429/149711036-67caab5d-6cb8-467a-b259-4c9fa2afc09c.png">

<img width="1323" alt="Screen Shot 2022-01-17 at 00 05 06" src="https://user-images.githubusercontent.com/49216429/149711020-76d2f99a-5723-4a19-92a4-92ebef50eddb.png">

```
class Solution:
    def combinationSum2(self, candidates, target):

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq-1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        backtrack(comb = [], remain = target, curr = 0,
                  counter = counter, results = results)

        return results
```

- Approach2: BackTracking with Index

<img width="1294" alt="Screen Shot 2022-01-17 at 00 06 59" src="https://user-images.githubusercontent.com/49216429/149711154-9af0bac9-5ded-4280-a2bb-bba3f475c022.png">
