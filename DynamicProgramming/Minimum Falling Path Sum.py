### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0900-0999/0931.Minimum%20Falling%20Path%20Sum/README.md



### Decription:
# 给你一个 n x n 的 方形 整数数组 matrix ，
# 请你找出并返回通过 matrix 的下降路径的最小和 。
# 下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
# 在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
# 具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。



### Example:
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：下面是两条和最小的下降路径，用加粗标注：
# [[2,"1",3],      [[2,"1",3],
#  [6,"5",4],       [6,5,"4"],
#  ["7",8,9]]       [7,"8",9]]

# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：下面是一条和最小的下降路径，用加粗标注：
# [["-19",57],
#  ["-40",-5]]

# 输入：matrix = [[-48]]
# 输出：-48



### Solution:
# https://leetcode-cn.com/problems/minimum-falling-path-sum/solution/cong-xia-wang-shang-si-kao-de-dong-tai-g-0z1m/
class Solution:
    def minFallingPathSum(self, matrix):
        dp = [[999999] * len(matrix) for _ in range(len(matrix))]  # 设置一个大值防干扰
        for i in range(len(matrix)):
            dp[0][i] = matrix[0][i]  # 第一行不涉及到前面的参数, 所以直接更新出来

        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                if j == 0:  # 等于零是在最左边， 此时只有正上和右上有值可取
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]

                elif j == len(matrix)-1:  # 等于len是在最右边， 此时只有正上和左上有值可取
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]

                else:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1]) + matrix[i][j]
        return min(dp[len(matrix)-1])
# 时间，空间复杂度均为O（n^2）, 在设置中间值存储追踪的情况下， 空间复杂度可以优化为O(n)



# https://leetcode-cn.com/problems/minimum-falling-path-sum/solution/dong-tai-gui-hua-yi-ci-bian-li-wu-e-wai-jwihf/
class Solution:
    def minFallingPathSum(self, matrix):
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == len(matrix[0])-1:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        return min(matrix[-1])



