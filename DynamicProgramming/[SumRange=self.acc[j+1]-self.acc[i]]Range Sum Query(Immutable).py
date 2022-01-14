# https://leetcode.com/problems/range-sum-query-immutable/



### Description:
# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:
# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) 
# Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).



### Examples:
# Input
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# Output
# [null, 1, -1, -3]

# Explanation
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
# numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
# numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3



### Solution:
# https://leetcode.com/problems/range-sum-query-immutable/discuss/75184/5-lines-C%2B%2B-4-lines-Python

# Create an array acc that stores the accumulated sum for nums such that:
# acc[i] = nums[0] + ... + nums[i-1]
# Then just return acc[j+1] - acc[i] in sumRange

class NumArray(object):
    def __init__(self, nums):
        self.acc = [0]
        for num in nums: 
            self.acc.append(self.acc[-1] + num)

    def sumRange(self, i, j):
        return self.acc[j + 1] - self.acc[i]


numArray = NumArray(nums=[-2, 0, 3, -5, 2, -1])
print(numArray.sumRange(0, 2)) # 1
print(numArray.sumRange(2, 5)) # -1
print(numArray.sumRange(0, 5)) # -3
