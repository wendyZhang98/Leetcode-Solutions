### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0104.Maximum%20Depth%20of%20Binary%20Tree/README.md


### Description
# 给定一个二叉树，找出其最大深度
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


### Solution
# 递归遍历左右子树，求左右子树的最大深度+1即可
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l, r)
