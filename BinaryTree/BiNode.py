### Link:
# https://github.com/doocs/leetcode/blob/main/lcci/17.12.BiNode/README.md


### 将二叉搜索树转换为单链表


### Description
# 二叉树数据结构TreeNode可用来表示单向链表
# 其中 left 置空，right 为下一个链表节点
# 实现一个方法，把二叉搜索树转换为单向链表，要求值的顺序保持不变
# 转换操作应是原址的，也就是在原始的二叉搜索树上直接修改
# 返回转换后的单向链表的头节点
# 注意：本题相对原题稍作改动


### Example
# 输入： [4,2,5,1,3,null,6,0]
# 输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]


### Solution
# 递归将左子树、右子树转换为左、右链表 left 和 right
# 然后将左链表 left 的最后一个结点的 right 指针指向 root
# root 的 right 指针指向右链表 right
# 并将 root 的 left 指针值为空


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root):
        if root is None:
            return None
        left = self.convertBiNode(root.left)    # ENDING: root.(left)^N is None;
        right = self.convertBiNode(root.right)  # right: root.(left)^(N-1).right is None;
        if left is None:            # True
            root.right = right      # root.right=root.(left)^(N-1).right=right=None
            return root             # （N-1:left) return root=root.(left)^(N-1)

        res = left
        while left and left.right:
            left = left.right
        left.right = root
        root.right = right
        root.left = None
        return res
