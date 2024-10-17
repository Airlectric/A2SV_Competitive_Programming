from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        count = 1

        while len(q):
            node = q.popleft()

            if node.left:
                count += 1
                q.append(node.left)
            
            if node.right:
                count += 1
                q.append(node.right)

        return count

        
