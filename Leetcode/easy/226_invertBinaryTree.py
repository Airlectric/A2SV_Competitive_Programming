from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        
        q = deque()
        q.append(root)

        while len(q):
            node = q.popleft()

            if node.left and node.right:
                holder = node.left
                node.left = node.right
                node.right = holder
            elif node.left and not node.right:
                node.right = node.left
                node.left = None
            elif node.right and not node.left:
                node.left = node.right
                node.right = None

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return root

        
        
        
