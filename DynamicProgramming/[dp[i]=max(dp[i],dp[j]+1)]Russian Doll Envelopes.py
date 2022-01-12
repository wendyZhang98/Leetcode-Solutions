### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0354.Russian%20Doll%20Envelopes/README.md




### Description:
# 给你一个二维整数数组 envelopes
# 其中 envelopes[i] = [wi, hi], 表示第 i 个信封的宽度和高度
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）
# 注意：不允许旋转信封




### Example:
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]

# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1




### Solution:
# https://github.com/doocs/leetcode/blob/main/solution/0300-0399/0354.Russian%20Doll%20Envelopes/README.md
# https://leetcode-cn.com/problems/russian-doll-envelopes/solution/e-luo-si-tao-wa-xin-feng-wen-ti-by-leetc-wj68/
# https://leetcode-cn.com/problems/russian-doll-envelopes/solution/tu-jie-e-luo-si-tao-wa-si-lu-qing-xi-dai-nbmv/

# 首先我们将所有的信封按照 w 值第一关键字升序、h 值第二关键字降序进行排序；
# 随后我们就可以忽略 w 维度，求出 h 维度的最长严格递增子序列，其长度即为答案。

class Solution:
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        nums = [x[1] for x in envelopes]
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res
