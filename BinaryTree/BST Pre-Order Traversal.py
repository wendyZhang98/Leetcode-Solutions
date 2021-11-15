### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0144.Binary%20Tree%20Preorder%20Traversal/README.md


### Description
# 给定一个二叉树的根节点root ，返回它的前序遍历


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ### Method1 : Recursion
    def preorderTraversal(self, root):
        def preorder(root):
            if root:
                res.append(root.val)
                preorder(root.left)
                preorder(root.right)
        res = []
        preorder(root)
        return res


    ### Method2 : Non-Recursion
    def preorderTraversal_(self, root):
        res = []
        if root:
            s = [root]
            while s:
                node = s.pop()
                res.append(node.val)
                if node.right:
                    s.append(node.right)
                if node.left:
                    s.append(node.left)
        return res


root = TreeNode(val=3,
                left=TreeNode(val=4, left=None, right=None),
                right=TreeNode(val=5, left=None, right=None))
pre_order_tree = Solution().preorderTraversal(root)
pre_order_tree_ = Solution().preorderTraversal_(root)
print(pre_order_tree)
print(pre_order_tree_)
