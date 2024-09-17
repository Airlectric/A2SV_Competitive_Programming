# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        stack = [(root, 1)]
        maxdepth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                maxdepth=max(maxdepth, depth)

                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return maxdepth
