### Descriptions:
- https://leetcode-cn.com/problems/container-with-most-water/

### Examples：
<img width="813" alt="Screen Shot 2022-07-11 at 11 06 06" src="https://user-images.githubusercontent.com/49216429/178295909-00c70975-efd6-45c9-8789-1a8d816c03e5.png">

### Solutions：
<img width="566" alt="Screen Shot 2022-02-24 at 16 42 29" src="https://user-images.githubusercontent.com/49216429/155612540-2b905017-674b-4980-961b-0ef1238a1df3.png">
<img width="792" alt="Screen Shot 2022-02-24 at 16 42 50" src="https://user-images.githubusercontent.com/49216429/155612596-3ada8c87-e863-42c9-a12f-f8a85e47b010.png">
<img width="782" alt="Screen Shot 2022-02-24 at 16 43 00" src="https://user-images.githubusercontent.com/49216429/155612625-817cb2ef-6bb7-4ef1-944b-3ab6fbdccd36.png">
<img width="792" alt="Screen Shot 2022-02-24 at 16 43 08" src="https://user-images.githubusercontent.com/49216429/155612646-36e1d2c6-6664-477b-816f-f2318843aa32.png">
<img width="688" alt="Screen Shot 2022-02-24 at 16 43 18" src="https://user-images.githubusercontent.com/49216429/155612663-88f106b2-5ee8-4c96-9490-b7a81b1bde69.png">
<img width="781" alt="Screen Shot 2022-02-24 at 16 43 29" src="https://user-images.githubusercontent.com/49216429/155612688-82df88e2-971c-4d83-9e93-4f1c142ea4d5.png">
<img width="784" alt="Screen Shot 2022-02-24 at 16 43 36" src="https://user-images.githubusercontent.com/49216429/155612706-bed2888c-72d4-4e95-9e2c-90bf38e20d85.png">
<img width="786" alt="Screen Shot 2022-02-24 at 16 43 47" src="https://user-images.githubusercontent.com/49216429/155612726-517c308e-8103-4321-beba-552c536de8ca.png">
<img width="796" alt="Screen Shot 2022-02-24 at 16 43 55" src="https://user-images.githubusercontent.com/49216429/155612738-49d8f97c-0e72-4f9d-bc1a-1f8233b42605.png">
<img width="805" alt="Screen Shot 2022-02-24 at 16 44 09" src="https://user-images.githubusercontent.com/49216429/155612768-b4b29bbb-762e-4602-a58a-e0abec09ba16.png">

```
class Solution(object):
    def maxArea(self, height):
        L, R, width, res = 0, len(height)-1, len(height)-1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res
```

### Complexity Analysis:
<img width="521" alt="Screen Shot 2022-02-24 at 16 56 23" src="https://user-images.githubusercontent.com/49216429/155614277-3892343d-7803-434f-96ef-48ea842c6454.png">
