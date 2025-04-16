from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque()
        q.append(root)
        big_arr = []

        while len(q):
            small_arr = []
            size = len(q)
            print(size)

            for _ in range(size):
                node = q.popleft()
                small_arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            big_arr.append(small_arr)
        return big_arr




    
        
