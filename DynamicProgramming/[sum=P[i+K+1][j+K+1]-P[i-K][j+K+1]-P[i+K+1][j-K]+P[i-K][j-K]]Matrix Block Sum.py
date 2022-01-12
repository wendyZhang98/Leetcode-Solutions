### Link:
# https://github.com/doocs/leetcode/blob/main/solution/1300-1399/1314.Matrix%20Block%20Sum/README_EN.md
# https://leetcode-cn.com/problems/matrix-block-sum/solution/ju-zhen-qu-yu-he-by-leetcode-solution/




### Description:
# 给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer
# 其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和：
# i - K <= r <= i + K, j - K <= c <= j + K
# (r, c) 在矩阵内




### Example:
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]

# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]




### Solution:
# 本题需要用到一些二维前缀和（prefix sum）知识

# 用 pre 表示数组 mat 的二维前缀和
# pre 的维数为（m+1）*（n+1）
# 其中 pre[i][j]表示数组 mat 中以（0，0）为左上角，（i-1，j-1）为右下角的矩阵子数组的元素之和

# 题目需要对数组 mat 中每个位置
# 计算以（i-K, j-K）为左上角，（i+K, j+K)为右下角的矩阵子数组的元素之和
# 我们可以在前缀数组和的帮助下计算 sum
# sum = P[i + K + 1][j + K + 1] - P[i - K][j + K + 1] - P[i + K + 1][j - K] + P[i - K][j - K]

# 得到元素之和。注意到 i + K + 1、j + K - 1、i - K 和 j - K 这些下标有可能不在矩阵内
# 因此对于所有的横坐标，我们需要将其规范在 [0, m] 的区间内
# 对于所有的纵坐标，我们需要将其规范在 [0, n] 的区间内。

# 具体地：
# i + K + 1 和 j + K - 1 分别可能超过 m 和 n
# 因此我们需要对这两个坐标与 m 和 n 取较小值，忽略不在矩阵内的部分
# i - K 和 j - K 可能小于 0
# 因此我们需要对这两个坐标与 0 取较大值，忽略不在矩阵内的部分

# 更一般的做法是，我们对所有的横坐标与 m 取较小值，纵坐标与 n 取较小值，
# 再将所有坐标与 0 取较大值，就可以将这些坐标规范在前缀和数组 P 的范围内。

class Solution:
    def matrixBlockSum(self, mat, K):
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) \
                            - get(i - K, j + K + 1) \
                            - get(i + K + 1, j - K) \
                            + get(i - K, j - K)
        return ans

print(Solution().matrixBlockSum(mat=[[1,2,3],[4,5,6],[7,8,9]], K=2))
