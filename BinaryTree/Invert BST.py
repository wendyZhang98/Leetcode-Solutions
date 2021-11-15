### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0200-0299/0226.Invert%20Binary%20Tree/README.md


### Description:
# 翻转一棵二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
