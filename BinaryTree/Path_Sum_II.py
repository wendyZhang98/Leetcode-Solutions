### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0113.Path%20Sum%20II/README.md


### Description
# 给你二叉树的根节点 root 和一个整数目标和 targetSum
# 找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径


### Example
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]

# 输入：root = [1,2,3], targetSum = 5
# 输出：[]

# 输入：root = [1,2], targetSum = 0
# 输出：[]


### Solution
# 深度优先搜索 + 路径记录


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, sum):
        def dfs(root, sum):
            if root is None:
                return
            path.append(root.val)
            if root.val == sum and root.left is None and root.right is None:
                res.append(path.copy())
            dfs(root.left, sum-root.val)
            dfs(root.right, sum-root.val)
            path.pop()
        if not root:
            return []
        res = []
        path = []
        dfs(root, sum)
        return res


root=TreeNode(val=5,\
              left=TreeNode(val=4,\
                            left=TreeNode(val=11, left=TreeNode(val=7, left=None, right=None),\
                            right=TreeNode(val=2, left=None, right=None)), right=None),\
              right=TreeNode(val=8,\
                             left=TreeNode(val=13, left=None, right=None),\
                             right=TreeNode(val=4, left=None, right=TreeNode(val=1, left=None, right=None))))


print(Solution().pathSum(root, 22))