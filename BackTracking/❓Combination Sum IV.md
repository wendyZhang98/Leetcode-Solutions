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
- At the first glance, the problem seems to be yet another combination-sum problem, as we have seen several examples before, e.g. Combination Sum, Combination Sum II, and Combination Sum III. However, the nature of this problem is very different from the previous combination-sum problems. The essential algorithm to solve the previous combination-sum problems is called Backtracking. While for this problem, we should apply the Dynamic Programming algorithm, as one will discover later.
- As a matter of fact, this problem can be considered as a variant of another problem called Coin Changes II. The prolem shares so many similarities with the Coin Changes II problem, to an extent that by switching the order of loops in one of the solutions of Coin Changes II, one could solve this problem.

- Approach1: Top-Down Dynamic Programming

<img width="1189" alt="Screen Shot 2022-01-17 at 16 48 51" src="https://user-images.githubusercontent.com/49216429/149840432-733e0e05-0c94-4914-9624-9c9eb37ed550.png">
<img width="1198" alt="Screen Shot 2022-01-17 at 16 51 15" src="https://user-images.githubusercontent.com/49216429/149840612-72a3d45c-d789-4425-b527-ea5373b1a1f2.png">
<img width="1181" alt="Screen Shot 2022-01-17 at 16 56 08" src="https://user-images.githubusercontent.com/49216429/149841015-f6a19a62-2754-45d2-85b6-c17cc952be03.png">

