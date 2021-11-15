### Link:
# https://github.com/doocs/leetcode/blob/main/lcof/%E9%9D%A2%E8%AF%95%E9%A2%9826.%20%E6%A0%91%E7%9A%84%E5%AD%90%E7%BB%93%E6%9E%84/README.md


### Description:
# 输入两棵二叉树A和B，判断B是不是A的子结构
# (约定空树不是任意一个树的子结构)
# B是A的子结构，即A中有出现和B相同的结构和节点值


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B):
        # check
        # from A, whether the path contains B
        def sub(A, B):
            if B is None:
                return True
            if A is None:
                return False
            return A.val == B.val and sub(A.left, B.left) and sub(A.right, B.right)

        if B is None or A is None:
            # the empty tree isn't the sub-structure of any tree
            return False

        if A.val != B.val:
            return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

        return sub(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
