### Descriptions:
https://leetcode.com/problems/squares-of-a-sorted-array/
<img width="630" alt="Screen Shot 2022-02-25 at 12 22 09" src="https://user-images.githubusercontent.com/49216429/155759246-b08f8a97-cbf1-445e-a5f7-05adfc609efe.png">

### Examples:
<img width="624" alt="Screen Shot 2022-02-25 at 12 50 34" src="https://user-images.githubusercontent.com/49216429/155763142-bdc98c57-19d1-4208-81e9-67b39cc01b61.png">


### Solutions:
<img width="612" alt="Screen Shot 2022-02-25 at 12 54 36" src="https://user-images.githubusercontent.com/49216429/155763706-fbc2bc0b-92a7-40e6-9558-b6f7b1916cdf.png">

```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
```
