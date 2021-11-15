### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0102.Binary%20Tree%20Level%20Order%20Traversal/README.md


### Description:
# 给你一个二叉树，请你返回其按层序遍历得到的节点值
# （即逐层地，从左到访问所有节点）


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        q = []
        q.append(root)
        while q:
            size = len(q)
            t = []
            for _ in range(size):
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                t.append(node.val)
            res.append(t)
        return res
