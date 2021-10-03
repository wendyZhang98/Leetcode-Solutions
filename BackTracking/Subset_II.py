### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0090.Subsets%20II/README.md
# https://leetcode-cn.com/problems/subsets-ii/solution/90-zi-ji-iiche-di-li-jie-zi-ji-wen-ti-ru-djmf/


### Description:
# 给你一个整数数组nums，其中可能包含重复元素
# 请你返回该数组所有可能的子集（幂集）
# 解集 不能 包含重复的子集
# 返回的解集中，子集可以按 任意顺序 排列


### Example:
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

# 输入：nums = [0]
# 输出：[[],[0]]


import copy
class Solution:
    def subsetsWithDup(self, nums):
        def dfs(nums, i, res, path):
            res.append(copy.deepcopy(path))
            for j in range(i, len(nums)):
                if j != i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(nums, j + 1, res, path)
                path.pop()
        res, path = [], []
        nums.sort()
        dfs(nums, 0, res, path)
        return res
