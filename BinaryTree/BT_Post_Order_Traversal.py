### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0145.Binary%20Tree%20Postorder%20Traversal/README.md


### Description
# 给定一个二叉树的根节点root ，返回它的后序遍历


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ### Method1 : Recursion
    def postorderTraversal(self, root):
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)
        res = []
        postorder(root)
        return res


    ### Method2 : Non-Recursion
    def postorderTraversal_(self, root):
        if not root:
            return []
        s1 = [root]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node.val)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        return s2[::-1]


root = TreeNode(val=3,
                left=TreeNode(val=4, left=None, right=None),
                right=TreeNode(val=5, left=None, right=None))
post_order_tree = Solution().postorderTraversal(root)
post_order_tree = Solution().postorderTraversal_(root)
print(post_order_tree)
print(post_order_tree)