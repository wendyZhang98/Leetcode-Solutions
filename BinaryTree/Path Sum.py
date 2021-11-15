### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0112.Path%20Sum/README.md


### Description
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum


### Example
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true

# 输入：root = [1,2,3], targetSum = 5
# 输出：false

# 输入：root = [1,2], targetSum = 0
# 输出：false


### Solution
# 递归求解：递归询问树的子节点是否能满足条件即可


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, sum):
        def dfs(root, sum):
            if root is None:
                return False
            if root.val == sum and root.left is None and root.right is None:  # Leaf Node
                return True
            return dfs(root.left, sum-root.val) or dfs(root.right, sum-root.val)  # True or False: True
        return dfs(root, sum)


root=TreeNode(val=5, \
              left=TreeNode(val=4,\
                            left=TreeNode(val=11, left=TreeNode(val=7, left=None, right=None),\
                            right=TreeNode(val=2, left=None, right=None)), right=None),\
              right=TreeNode(val=8,\
                             left=TreeNode(val=13, left=None, right=None),\
                             right=TreeNode(val=4, left=None, right=TreeNode(val=1, left=None, right=None))))


print(Solution().hasPathSum(root, 22))
