### Descirption:
https://leetcode.com/problems/sqrtx/
<img width="1041" alt="Screen Shot 2022-02-24 at 00 29 28" src="https://user-images.githubusercontent.com/49216429/155463785-33c8c1af-1bf2-41a6-967b-4c5746bf3f58.png">
<img width="1015" alt="Screen Shot 2022-02-24 at 00 30 01" src="https://user-images.githubusercontent.com/49216429/155463846-75adba4d-368a-40ba-a0d8-cc754e89ae90.png">
<img width="922" alt="Screen Shot 2022-02-24 at 00 39 31" src="https://user-images.githubusercontent.com/49216429/155464805-2643e8bc-421d-4272-8a01-cf8f83f7fda4.png">
<img width="742" alt="Screen Shot 2022-02-24 at 00 40 06" src="https://user-images.githubusercontent.com/49216429/155464866-9b18883a-03db-4a5e-9508-526674125027.png">

```
class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        return right
```
