### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0257.Binary%20Tree%20Paths/README.md


### Description
# 给定一个二叉树，返回所有从根节点到叶子节点的路径
# 说明: 叶子节点是指没有子节点的节点


### 深度优先搜索 + 路径记录
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        def dfs(root):
            if root is None:
                return
            path.append(str(root.val))
            if root.left is None and root.right is None:
                res.append("->".join(path))
            dfs(root.left)
            dfs(root.right)
            path.pop()

        res = []
        path = []
        dfs(root)
        return res