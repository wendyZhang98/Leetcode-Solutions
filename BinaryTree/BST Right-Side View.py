### Link:
# https://github.com/doocs/leetcode/blob/main/solution/0100-0199/0199.Binary%20Tree%20Right%20Side%20View/README.md


### Description:
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值


### Leetcode Solution Link:
# https://leetcode-cn.com/problems/binary-tree-right-side-view/solution/er-cha-shu-de-you-shi-tu-by-leetcode-solution/


### Solution1 : Depth-First Search
# 我们对二叉树进行深度优先搜索，在搜索过程中，我们总是先访问右子树
# 那么对于每一层来说，我们在这层见到的第一个结点一定是最右边的结点


class Solution:
    def rightSideView(self, root):

        # depth : node
        rightmost_value_at_depth = dict()
        max_depth = -1

        # stack : (node, depth)
        stack = [(root, 0)]

        while stack:
            node, depth = stack.pop()

            if node is not None:
                # maintain/update the max_depth of the BT
                max_depth = max(max_depth, depth)

                # if depth doesn't exist in dict, insert (depth, node.val)
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]


### Solution2 : Breadth-First Search
# 我们可以对二叉树进行层次遍历，那么对于每层来说
# 最右边的结点一定是最后被遍历到的
# 二叉树的层次遍历可以用广度优先搜索实现

from collections import deque

class Solution:
    def rightSideView(self, root):

        # depth : node
        rightmost_value_at_depth = dict()
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                # maintain/update the max_depth of the BT
                max_depth = max(max_depth, depth)

                # only the last visited node is the answer that we want
                # thus we just need to continue updating the depth info
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]



# from collections import deque
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def rightSideView(self, root):
#         if not root:
#             return []
#         q = deque([root])
#         res = []
#         while q:
#             size = len(q)
#             res.append(q[0].val)
#             for _ in range(size):
#                 node = q.popleft()
#                 if node.right:
#                     q.append(node.right)
#                 if node.left:
#                     q.append(node.left)
#         return res



