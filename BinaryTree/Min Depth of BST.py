### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0111.Minimum%20Depth%20of%20Binary%20Tree/README.md


### Description
# 给定一个二叉树，找出其最小深度
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量
# 说明：叶子节点是指没有子节点的节点


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


### Method 1
### 深度优先搜索

# 首先可以想到使用深度优先搜索的方法，遍历整棵树，记录最小深度
# 对于每一个非叶子节点，我们只需要分别计算其左右子树的最小叶子节点深度
# 这样就将一个大问题转化为了小问题，可以递归地解决该问题

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1


### Method 2
### 广度优先搜索

# 同样，我们可以想到使用广度优先搜索的方法，遍历整棵树
# 当我们找到一个叶子节点时，直接返回这个叶子节点的深度
# 广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小

import collections

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
    # deque in python
    # https: // www.geeksforgeeks.org / deque - in -python /

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        return 0
