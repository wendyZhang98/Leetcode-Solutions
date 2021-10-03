### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0078.Subsets/README.md


### Description:
# 给你一个整数数组nums，数组中的元素互不相同
# 返回该数组所有可能的子集（幂集）
# 解集不能包含重复的子集
# 你可以按任意顺序返回解集


### Example:
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# 输入：nums = [0]
# 输出：[[],[0]]


### 模版
# res = []
# path = []
# def backtrack(未探索区域, res, path):
#     if path 满足条件:
#         res.add(path) # 深度拷贝
#         # return  # 如果不用继续搜索需要 return
#     for 选择 in 未探索区域当前可能的选择:
#         if 当前选择符合要求:
#             path.add(当前选择)
#             backtrack(新的未探索区域, res, path)
#             path.pop()


import copy
class Solution:
    def subsets(self, nums):
        def dfs(nums, i, res, path):
            res.append(copy.deepcopy(path))
            while i<len(nums):
                path.append(nums[i])
                dfs(nums, i+1, res, path)
                path.pop()
                i+=1

        res, path = [], []
        dfs(nums, 0, res, path)
        return res

print(Solution().subsets(nums = [1,2,3]))


## https://leetcode-cn.com/problems/subsets/solution/dai-ma-sui-xiang-lu-78-zi-ji-hui-su-sou-6yfk6/
class Solution:
    def subsets(self, nums):
        res = []
        path = []
        def backtrack(nums, startIndex):
            res.append(path[:])
            for i in range(startIndex, len(nums)):
                path.append(nums[i])
                backtrack(nums, i+1)
                path.pop()
        backtrack(nums, 0)
        return res
