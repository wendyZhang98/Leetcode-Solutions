### Descriptions:
- Link: https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
- Given an array of N integers and an integer K
- Find the number of pairs of elements in the array whose sum is equal to K


### Examples: 
#1
- Input: N = 4, K = 6; Arr[] = {1, 5, 7, 1}
- Output: 2
- arr[0] + arr[1] = 1 + 5 = 6 
- arr[1] + arr[3] = 5 + 1 = 6.

#2
- N = 4, X = 2
- Arr[] = {1, 1, 1, 1}
- Output: 6
- Each 1 will produce sum 2 with any 1.



### Solutions:
```
class Solution:
    def getPairsCount(self, arr, n, sum):
        m = dict()
        for i in range(n):
            if arr[i] in m.keys():
                m[arr[i]] += 1
            else:
                m[arr[i]] = 1
        twice_count = 0
 
        # Iterate through each element and increment the count 
        # Notice that every pair is counted twice
        for i in range(0, n):
            if sum-arr[i] in m.keys():
                twice_count += m[sum-arr[i]]
 
            # if (arr[i], arr[i]) pair satisfies the condition
            # then we need to ensure that the count is decreased by one 
            # such that the (arr[i], arr[i]) pair is not considered
            if sum-arr[i] == arr[i]:
                twice_count -= 1
 
        # return the half of twice_count
        return int(twice_count / 2)
        
print(Solution().getPairsCount(arr=[1, 5, 7, 1], n=4, sum=6))
```
