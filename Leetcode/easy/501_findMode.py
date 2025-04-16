from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append(root)
        count = {}

        while len(q):
            node = q.popleft()
            if node:
                count[node.val] = count.get(node.val, 0) + 1
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)

        max_val = max(count.values())
        res = []
        for key in count.keys():
            if count[key] == max_val:
                res.append(key)

        return res


        
