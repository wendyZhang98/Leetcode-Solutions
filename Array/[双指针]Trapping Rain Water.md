### Descriptions:
https://leetcode.com/problems/trapping-rain-water/
<img width="626" alt="Screen Shot 2022-02-24 at 17 04 14" src="https://user-images.githubusercontent.com/49216429/155615275-a256ecc7-d9c9-4727-88ab-fb900c6fa403.png">

### Examples:
<img width="629" alt="Screen Shot 2022-02-24 at 17 04 26" src="https://user-images.githubusercontent.com/49216429/155615302-286ddaad-ca1e-4c71-b00d-0f441c0731fa.png">

### Solutions:
<img width="626" alt="Screen Shot 2022-02-24 at 17 04 58" src="https://user-images.githubusercontent.com/49216429/155615390-332db3ba-d915-4b15-be55-0807860c0a98.png">
<img width="537" alt="Screen Shot 2022-02-24 at 17 11 24" src="https://user-images.githubusercontent.com/49216429/155616104-7574aa07-56ef-4e73-9bf9-d56e8bb9018e.png">
<img width="576" alt="Screen Shot 2022-02-24 at 17 15 21" src="https://user-images.githubusercontent.com/49216429/155616586-d0513fd1-13ff-4093-b472-ba34c9d4ce7e.png">
<img width="561" alt="Screen Shot 2022-02-24 at 17 15 31" src="https://user-images.githubusercontent.com/49216429/155616599-3ffa1014-1086-459f-aba6-cdfa3fc0e90f.png">
<img width="546" alt="Screen Shot 2022-02-24 at 17 15 45" src="https://user-images.githubusercontent.com/49216429/155616630-6e0dd82b-817b-408c-bc8c-69821500dc5f.png">
<img width="541" alt="Screen Shot 2022-02-24 at 17 15 53" src="https://user-images.githubusercontent.com/49216429/155616643-b3cb1d76-25c1-4aed-ac86-73447d114517.png">
<img width="567" alt="Screen Shot 2022-02-24 at 17 16 13" src="https://user-images.githubusercontent.com/49216429/155616692-08c30b38-0d74-4d11-a992-414fcb1aee10.png">
<img width="534" alt="Screen Shot 2022-02-24 at 17 16 24" src="https://user-images.githubusercontent.com/49216429/155616703-acc483a5-2a07-4c59-97d1-b505ed05e45d.png">
<img width="542" alt="Screen Shot 2022-02-24 at 17 16 33" src="https://user-images.githubusercontent.com/49216429/155616719-f727beeb-5da1-4b71-af1b-3bf2f0a8e8c9.png">
<img width="536" alt="Screen Shot 2022-02-24 at 17 16 43" src="https://user-images.githubusercontent.com/49216429/155616734-044d0f42-0e1c-4cdc-aeeb-3e96d2012ae0.png">
<img width="558" alt="Screen Shot 2022-02-24 at 17 16 49" src="https://user-images.githubusercontent.com/49216429/155616745-7f02d277-9de6-4e28-b3bd-a0815ff4fb28.png">
<img width="548" alt="Screen Shot 2022-02-24 at 17 16 57" src="https://user-images.githubusercontent.com/49216429/155616756-5504f60c-9ced-4e1a-a259-86771da0f176.png">

```
class Solution:
# @param A, a list of integers
# @return an integer
    def trap(self, arr):
        left = right = water = 0
        i, j = 0, len(arr)-1
        while i <= j:
            left, right = max(left, arr[i]), max(right, arr[j])
            while i <= j and arr[i] <= left <= right:
                water += left - arr[i]
                i += 1
            while i <= j and arr[j] <= right <= left:
                water += right - arr[j]
                j -= 1
        return water
```

### Complexity Analysis:
<img width="615" alt="Screen Shot 2022-02-24 at 17 18 25" src="https://user-images.githubusercontent.com/49216429/155616926-2d4c0f87-5154-4482-bcda-0ee983488102.png">
