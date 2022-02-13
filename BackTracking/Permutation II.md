https://leetcode.com/problems/permutations-ii/



### Description:
- Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.




### Examples:
|Input|Output|
|---|---|
|[1,1,2]|[[1,1,2],[1,2,1],[2,1,1]]|
|[1,2,3]|[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]|




### Solutions:
<img width="1346" alt="Screen Shot 2022-01-17 at 23 53 12" src="https://user-images.githubusercontent.com/49216429/149873093-4dc74cbd-5ca2-4038-9209-9b7f8cbdd761.png">
<img width="1329" alt="Screen Shot 2022-01-17 at 23 53 28" src="https://user-images.githubusercontent.com/49216429/149873120-e883d764-eab4-4fa6-81c4-b4f72174ea97.png">
<img width="1336" alt="Screen Shot 2022-01-17 at 23 53 51" src="https://user-images.githubusercontent.com/49216429/149873150-bd58f0fe-9cc0-4550-8fd1-89ce559802aa.png">

```
class Solution:
    def permuteUnique(self, nums):
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results
```
