### Descriptioins:
https://leetcode.com/problems/koko-eating-bananas/
<img width="1097" alt="Screen Shot 2022-02-24 at 14 49 57" src="https://user-images.githubusercontent.com/49216429/155596794-3139fd08-1069-4dba-8c11-af3348ea84f9.png">

### Examples:
<img width="1119" alt="Screen Shot 2022-02-24 at 14 52 46" src="https://user-images.githubusercontent.com/49216429/155597164-e32e6057-12c0-4289-b680-90967b76bad0.png">


### Solutions:
<img width="1121" alt="Screen Shot 2022-02-24 at 14 54 10" src="https://user-images.githubusercontent.com/49216429/155597378-0ee15744-11a6-42af-87d6-749cf113a6e5.png">
<img width="1110" alt="Screen Shot 2022-02-24 at 14 54 18" src="https://user-images.githubusercontent.com/49216429/155597403-b82cd794-a3f2-4873-b68b-7b53f4b03b01.png">
<img width="1132" alt="Screen Shot 2022-02-24 at 14 57 44" src="https://user-images.githubusercontent.com/49216429/155597931-2fbb6497-7e6b-4946-b3fe-2a7972d13668.png">
<img width="1114" alt="Screen Shot 2022-02-24 at 14 57 53" src="https://user-images.githubusercontent.com/49216429/155597952-64c7cdde-d412-4119-a162-ae3cadb516f2.png">

```
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:  
        # Initalize the left and right boundaries     
        left = 1
        right = max(piles)
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # hour_spent stands for the total hour Koko spends.
            middle = (left + right) // 2            
            hour_spent = 0
            
            # Iterate over the piles and calculate hour_spent.
            # We increase the hour_spent by ceil(pile / middle)
            for pile in piles:
                hour_spent += math.ceil(pile / middle)
            
            # Check if middle is a workable speed, and cut the search space by half.
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        # Once the left and right boundaries coincide, we find the target value,
        # that is, the minimum workable eating speed.
        return right
```

### Complexity Analysis:
<img width="1106" alt="Screen Shot 2022-02-24 at 14 58 46" src="https://user-images.githubusercontent.com/49216429/155598060-40ec2145-f270-485a-8443-af039cc74e30.png">
