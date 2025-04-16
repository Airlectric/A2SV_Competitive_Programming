from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 
            
        q = deque()
        q.append(root)
        leftSum = 0

        while len(q):
            node = q.popleft()

            if node.left:
                q.append(node.left)
                if not node.left.left and not node.left.right:
                    leftSum += node.left.val

            if node.right:
                q.append(node.right)

        return leftSum
        
