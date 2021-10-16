### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0118.Pascal%27s%20Triangle/README_EN.md



### Description:
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行
# 在杨辉三角中，每个数是它左上方和右上方的数的和



### Example:
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]



### Solution:
# 先设置每一行首尾元素为 1，其它元素为 0
# 然后根据杨辉三角，设置每一行其它元素即可

class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            t = [1 if j == 0 or j == i else 0 for j in range(i + 1)]
            for j in range(1, i):
                t[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(t)
        return res

print(Solution().generate(numRows=10))