### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0000-0099/0094.Binary%20Tree%20Inorder%20Traversal/README.md


### Description
# 给定一个二叉树的根节点root ，返回它的中序遍历


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ### Method1 : Recursion
    def inorderTraversal(self, root):
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        res = []
        inorder(root)
        return res


    ### Method2 : Non-Recursion
    def inorderTraversal_(self, root):
        s = []
        res = []
        while root or s:
            if root:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                res.append(root.val)
                root = root.right
        return res


root = TreeNode(val=3,
                left=TreeNode(val=4, left=None, right=None),
                right=TreeNode(val=5, left=None, right=None))
in_order_tree = Solution().inorderTraversal(root)
in_order_tree_ = Solution().inorderTraversal_(root)
print(in_order_tree)
print(in_order_tree_)
