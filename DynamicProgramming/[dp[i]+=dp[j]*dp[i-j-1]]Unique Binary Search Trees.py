### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0096.Unique%20Binary%20Search%20Trees/README.md



### Description:
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3




### Solution:
# 假设 n 个节点存在二叉搜索树的个数是 G(n)，1 为根节点，2 为根节点，...，n 为根节点，
# 当 1 为根节点时，其左子树节点个数为 0，右子树节点个数为 n-1，
# 同理当 2 为根节点时，其左子树节点个数为 1，右子树节点为 n-2，
# 所以可得 G(n) = G(0) * G(n-1) + G(1) * (n-2) + ... + G(n-1) * G(0)。

class Solution:
    def numTrees(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


print(Solution().numTrees(n=3))   # 5

print(Solution().numTrees(n=10))  # 16796
