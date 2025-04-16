from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return 0

        q = deque()
        q.append(root)
        arr = []

        while len(q):
            sum = 0
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                sum+=node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(float(sum)/float(size))
        return arr

                
            

        
