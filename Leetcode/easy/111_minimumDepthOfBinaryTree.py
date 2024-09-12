from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        q = deque()
        q.append(root)
        level = 0

        while len(q):
            size = len(q)
            level+=1

            for _ in range(size):
                node = q.popleft()

                if not node.left and not node.right:
                    return level

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)



        
