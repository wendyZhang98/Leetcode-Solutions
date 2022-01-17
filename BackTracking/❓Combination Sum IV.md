- https://leetcode.com/problems/combination-sum-iv/
  
  
  
### Decription:
- Given an array of distinct integers nums and a target integer target, 
- return the number of possible combinations that add up to target.
- The test cases are generated so that the answer can fit in a 32-bit integer.

 

### Examples:
|Input|Output|
|---|---|
|nums = [1,2,3], target = 4|(1, 1, 1, 1),(1, 1, 2),(1, 2, 1),(1, 3),(2, 1, 1),(2, 2),(3, 1)|
|nums = [9], target = 3|0|



### Solutions:
- Overview:
- At the first glance, the problem seems to be yet another combination-sum problem, 
- as we have seen several examples before, e.g. Combination Sum, Combination Sum II, and Combination Sum III.
- However, the nature of this problem is very different from the previous combination-sum problems.
- The essential algorithm to solve the previous combination-sum problems is called Backtracking. 
- While for this problem, we should apply the Dynamic Programming algorithm, as one will discover later.


