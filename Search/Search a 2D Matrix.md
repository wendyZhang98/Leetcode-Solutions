### Descriptions:
https://leetcode.com/problems/search-a-2d-matrix/
<img width="980" alt="Screen Shot 2022-02-24 at 00 44 05" src="https://user-images.githubusercontent.com/49216429/155465302-35c5bdef-49c0-495c-8128-5f1ede76852b.png">


### Solutions:
<img width="1114" alt="Screen Shot 2022-02-24 at 00 44 40" src="https://user-images.githubusercontent.com/49216429/155465360-8e38d1e2-0959-4029-be41-64a951fa8276.png">
<img width="1109" alt="Screen Shot 2022-02-24 at 00 45 07" src="https://user-images.githubusercontent.com/49216429/155465389-7d813eac-9dc4-4de8-ae7d-6d891b5b9324.png">

```
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False
```

### Complexity:
<img width="535" alt="Screen Shot 2022-02-24 at 00 47 26" src="https://user-images.githubusercontent.com/49216429/155465627-4e7706d2-7b74-4459-8234-53c6e72d668a.png">

