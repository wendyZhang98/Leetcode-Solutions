### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0173.Binary%20Search%20Tree%20Iterator/README.md


### Description:
# 实现一个二叉搜索树迭代器类BSTIterator
# 表示一个按中序遍历二叉搜索树（BST）的迭代器：

# BSTIterator(TreeNode root) 初始化 BSTIterator 类的一个对象
# BST 的根节点 root 会作为构造函数的一部分给出

# 指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素
# boolean hasNext() 如果向指针右侧遍历存在数字，则返回 true ；否则返回 false
# int next()将指针向右移动，然后返回指针处的数字

# 注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字


### Example
# 输入
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]

# 输出
# [null, 3, 7, true, 9, true, 15, true, 20, false]

# 解释
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
# bSTIterator.next();    // 返回 3
# bSTIterator.next();    // 返回 7
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 9
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 15
# bSTIterator.hasNext(); // 返回 True
# bSTIterator.next();    // 返回 20
# bSTIterator.hasNext(); // 返回 False


### Solution
# 初始化数据时，递归中序遍历，将二叉搜索树每个结点的值保存在列表 vals 中
# 用 cur/next 指针记录外部即将遍历的位置，初始化为 0
# 调用 next() 时，返回 vals[cur]，同时 cur 指针自增
# 调用 hasNext() 时，判断 cur 指针是否已经达到 vals 个数
# 若是，说明已经遍历结束，返回 false，否则返回 true


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            self.vals.append(root.val)
            inorder(root.right)

        self.cur = 0
        self.vals = []
        inorder(root)

    def next(self):
        res = self.vals[self.cur]
        self.cur += 1
        return res

    def hasNext(self):
        return self.cur < len(self.vals)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()