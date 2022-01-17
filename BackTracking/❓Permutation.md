https://leetcode.com/problems/permutations/



### Description:
- Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.




### Examples:
|Input|Output|
|---|---|
|Input: nums = [1,2,3]|Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]|
|Input: nums = [0,1]|Output: [[0,1],[1,0]]|
|Input: nums = [1]|Output: [[1]]|



### Solutions:
<img width="831" alt="Screen Shot 2022-01-17 at 18 17 17" src="https://user-images.githubusercontent.com/49216429/149846695-ba6ed4b6-5594-43fc-aa2c-d066d8d4e14a.png">

```
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output
```
