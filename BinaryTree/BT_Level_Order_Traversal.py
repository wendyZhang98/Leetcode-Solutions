### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0102.Binary%20Tree%20Level%20Order%20Traversal/README.md


### Description:
# 给定一个二叉树，返回其节点值自底向上的层序遍历
# （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        q = [root]
        res = []
        while q:
            size = len(q)
            t = []
            for _ in range(size):
                node = q.pop(0)
                t.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(t)
        return res[::-1]