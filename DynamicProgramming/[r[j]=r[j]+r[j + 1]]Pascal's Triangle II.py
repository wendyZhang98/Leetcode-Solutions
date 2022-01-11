### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0119.Pascal%27s%20Triangle%20II/README_EN.md



### Description:
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行
# 在杨辉三角中，每个数是它左上方和右上方的数的和

# 进阶：
# 你可以优化你的算法到 O(k) 空间复杂度吗？



### Example:
# 输入: 3
# 输出: [1,3,3,1]



### Solution:
# 对杨辉三角，有第i行与第i-1行的关系：
# i[j] = (i-1)[j-1] + (i-1)[j]
# 如果对第 i-1 行前面插上一个 0，那么：
# i[j] = (i-1)[j] + (i-1)[j+1]
# 那直接在前面插上0并持续迭代就好了。

# https://leetcode-cn.com/problems/pascals-triangle-ii/solution/119-yang-hui-san-jiao-ii-python-by-sanct-zich/
class Solution:
    def getRow(self, rowIndex):
        r = [1]
        for i in range(1, rowIndex + 1):
            r.insert(0, 0)
            for j in range(i):
                r[j] = r[j] + r[j + 1]
        return r

print(Solution().getRow(rowIndex=3))

print(Solution().getRow(rowIndex=10))



