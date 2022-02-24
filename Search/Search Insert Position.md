### Description:
- https://leetcode.com/problems/search-insert-position/
<img width="1224" alt="Screen Shot 2022-02-23 at 19 37 36" src="https://user-images.githubusercontent.com/49216429/155434710-c9205c92-bb55-499a-bb02-9bf87ec2392b.png">


### Examples:
<img width="1209" alt="Screen Shot 2022-02-23 at 19 37 51" src="https://user-images.githubusercontent.com/49216429/155434730-5b651bff-c64c-45eb-b4dc-6ff41b1121d0.png">


### Solutions:
<img width="1253" alt="Screen Shot 2022-02-23 at 19 41 46" src="https://user-images.githubusercontent.com/49216429/155435089-b51bb307-b5b9-41fd-8344-7da2179b4afe.png">
<img width="1196" alt="Screen Shot 2022-02-23 at 19 42 22" src="https://user-images.githubusercontent.com/49216429/155435140-9380efbf-3c5d-4158-b493-136bf293b4eb.png">
<img width="1294" alt="Screen Shot 2022-02-23 at 19 44 55" src="https://user-images.githubusercontent.com/49216429/155435368-4ff39d43-0cee-4493-afca-7ac2f18865b2.png">
<img width="1289" alt="Screen Shot 2022-02-23 at 19 46 23" src="https://user-images.githubusercontent.com/49216429/155435531-f7b5f231-2bb8-4668-b71f-889e263e7a65.png">
<img width="1257" alt="Screen Shot 2022-02-23 at 19 47 21" src="https://user-images.githubusercontent.com/49216429/155435643-e0b65618-8be4-4a21-9176-ee8d2046bdd5.png">
<img width="1155" alt="Screen Shot 2022-02-23 at 19 47 48" src="https://user-images.githubusercontent.com/49216429/155435691-ea2d3d49-3e0f-454c-a7fe-3aa64cc53608.png">

```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left
```

### Complexity Analysis:
<img width="1279" alt="Screen Shot 2022-02-23 at 19 52 26" src="https://user-images.githubusercontent.com/49216429/155436092-2e575eff-b3cd-48c0-b305-19f0836e1f71.png">


<img width="910" alt="Screen Shot 2022-02-23 at 19 56 35" src="https://user-images.githubusercontent.com/49216429/155436504-4bdb71bb-5fae-4426-81f1-304524e094a7.png">
