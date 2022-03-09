### Description:
- Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
- If target is not found in the array, return [-1, -1].
- You must write an algorithm with O(log n) runtime complexity.


### Examples:
<img width="782" alt="Screen Shot 2022-03-08 at 23 25 46" src="https://user-images.githubusercontent.com/49216429/157372547-73ea178a-318b-40a4-a709-d59bd5cb03b5.png">


### Solutions:
<img width="1051" alt="Screen Shot 2022-03-08 at 23 40 03" src="https://user-images.githubusercontent.com/49216429/157373974-55b66b70-6176-4fef-a18f-e323d562c24a.png">
<img width="1027" alt="Screen Shot 2022-03-08 at 23 41 20" src="https://user-images.githubusercontent.com/49216429/157374096-60f0b4ba-c1c1-4034-9df7-c2674e6b0073.png">
<img width="1027" alt="Screen Shot 2022-03-08 at 23 42 40" src="https://user-images.githubusercontent.com/49216429/157374216-fa775067-ef35-497b-b91a-ae282d06bec9.png">
<img width="1042" alt="Screen Shot 2022-03-08 at 23 45 38" src="https://user-images.githubusercontent.com/49216429/157374505-439ea1ff-000f-42db-b0e4-27803450c37d.png">
<img width="1040" alt="Screen Shot 2022-03-08 at 23 45 59" src="https://user-images.githubusercontent.com/49216429/157374547-e672c865-5d13-4359-8506-e86fa8bf9ab0.png">
<img width="1034" alt="Screen Shot 2022-03-08 at 23 46 31" src="https://user-images.githubusercontent.com/49216429/157374631-435c562e-153d-4d96-a6a3-d8c05dd7326c.png">
<img width="1046" alt="Screen Shot 2022-03-08 at 23 49 35" src="https://user-images.githubusercontent.com/49216429/157374953-bde935ee-2d37-446a-825f-b82e86d5dc38.png">

````
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findBound(nums, target, True)
        if (lower_bound == -1):
            return [-1, -1]
        
        upper_bound = self.findBound(nums, target, False)
        
        return [lower_bound, upper_bound]
        
    def findBound(self, nums: List[int], target: int, isFirst: bool) -> int:
        
        N = len(nums)
        begin, end = 0, N - 1
        while begin <= end:
            mid = int((begin + end) / 2)    
            
            if nums[mid] == target:
                
                if isFirst:
                    # This means we found our lower bound.
                    if mid == begin or nums[mid - 1] < target:
                        return mid

                    # Search on the left side for the bound.
                    end = mid - 1
                else:
                    
                    # This means we found our upper bound.
                    if mid == end or nums[mid + 1] > target:
                        return mid
                    
                    # Search on the right side for the bound.
                    begin = mid + 1
            
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1
        
### Complexity:
<img width="1036" alt="Screen Shot 2022-03-08 at 23 51 32" src="https://user-images.githubusercontent.com/49216429/157375145-c66247b7-86df-460f-ab43-e24013080963.png">
