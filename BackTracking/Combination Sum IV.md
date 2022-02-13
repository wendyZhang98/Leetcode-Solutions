- https://leetcode.com/problems/combination-sum-iv/
  
  
  
### Decription:
- Given an array of distinct integers nums and a target integer target, 
- return the number of possible combinations that add up to target.
- The test cases are generated so that the answer can fit in a 32-bit integer.

 

### Examples:
|Input|Output|
|---|---|
|nums = [1,2,3], target = 4|(1, 1, 1, 1),(1, 1, 2),(1, 2, 1),(1, 3),(2, 1, 1),(2, 2),(3, 1)|
|nums = [9], target = 3|0|



### Solutions:
- At the first glance, the problem seems to be yet another combination-sum problem, as we have seen several examples before, e.g. Combination Sum, Combination Sum II, and Combination Sum III. However, the nature of this problem is very different from the previous combination-sum problems. The essential algorithm to solve the previous combination-sum problems is called Backtracking. While for this problem, we should apply the Dynamic Programming algorithm, as one will discover later.
- As a matter of fact, this problem can be considered as a variant of another problem called Coin Changes II. The prolem shares so many similarities with the Coin Changes II problem, to an extent that by switching the order of loops in one of the solutions of Coin Changes II, one could solve this problem.

- Approach1: Top-Down Dynamic Programming

<img width="1189" alt="Screen Shot 2022-01-17 at 16 48 51" src="https://user-images.githubusercontent.com/49216429/149840432-733e0e05-0c94-4914-9624-9c9eb37ed550.png">
<img width="1198" alt="Screen Shot 2022-01-17 at 16 51 15" src="https://user-images.githubusercontent.com/49216429/149840612-72a3d45c-d789-4425-b527-ea5373b1a1f2.png">
<img width="1181" alt="Screen Shot 2022-01-17 at 16 56 08" src="https://user-images.githubusercontent.com/49216429/149841015-f6a19a62-2754-45d2-85b6-c17cc952be03.png">

```
class Solution:
    def combinationSum4(self, nums, target):
        # potential optimization
        # nums.sort()

        @functools.lru_cache(maxsize = None)
        def combs(remain):
            if remain == 0:
                return 1

            result = 0
            for num in nums:
                if remain - num >= 0:
                    result += combs(remain - num)
                # potential optimization
                # else:
                #     break

            return result

        return combs(target)
```

- Approach2: Bottom-Up Dynamic Programming
<img width="1192" alt="Screen Shot 2022-01-17 at 17 15 54" src="https://user-images.githubusercontent.com/49216429/149842610-a400ccbe-c30e-41c7-8cb4-c3a37fd29214.png">
<img width="1183" alt="Screen Shot 2022-01-17 at 17 16 06" src="https://user-images.githubusercontent.com/49216429/149842637-985a9680-5bfe-423b-8f44-0c62502d0371.png">
<img width="1168" alt="Screen Shot 2022-01-17 at 17 16 20" src="https://user-images.githubusercontent.com/49216429/149842647-598b7684-6592-4fa6-bf5d-01a81a2b617c.png">

```
class Solution:
    def combinationSum4(self, nums, target):
        # minor optimization
        # nums.sort()
        dp = [0 for i in range(target+1)]
        dp[0] = 1

        for comb_sum in range(target+1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum-num]
                # minor optimization, early stopping.
                # else:
                #    break
        return dp[target]
```

