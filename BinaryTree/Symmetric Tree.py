### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0101.Symmetric%20Tree/README.md


### Description:
# 给定一个二叉树，检查它是否是镜像对称的


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

### 递归
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.is_symmetric(root.left, root.right)

    def is_symmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.is_symmetric(left.left, right.right) and self.is_symmetric(left.right, right.left)
