### Link:
# https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1014.Best%20Sightseeing%20Pair/README.md


### Description:
# 给你一个正整数数组 values，其中values[i]表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i
# 一对景点（i < j）组成的观光组合的得分为 values[i] + values[j] + i - j ，也就是景点的评分之和 减去 它们两者之间的距离
# 返回一对观光景点能取得的最高分


### Example:
# 输入：A = [8, 1, 5, 2, 6]
# 输出：11
# 解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

# 输入：A = [1, 2]
# 输出：2



### Solution:
# 求 res = A[i] + A[j] + i - j (i<j) 的最大值
# 对于输入的每一个 A[j]来说，A[j]-j 是固定的
# 因此对每一个 A[j]来说，想求 res 的最大值，也就是求 A[i]+i (i<j) 的最大值
# 使用变量 pre_max 记录当前元素 A[j] 之前 A[i]+i 的最大值
# 因此对每一个 A[j]来说，最大得分 max_res = pre_max + A[j] - j
# 再从所有 A[j] 的 max_res 中挑选出最大值即可。


class Solution:
    def maxScoreSightseeingPair(self, A):
        # initialization
        res= 0
        pre_max = A[0] + 0
        
        for j in range(1, len(A)):
            res = max(res, values[j]-j+pre_max)  # 判断能否刷新 res
            pre_max = max(pre_max, values[j]+j) # 判断能否刷新 pre_max
        return res

    
print(Solution().maxScoreSightseeingPair(values = [8, 1, 5, 2, 6]))
