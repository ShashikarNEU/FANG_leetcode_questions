# FOLLOW UP TO LV ORDER

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        q.append(None)
        currentOrder = []
        lvOrder = []

        while q:
            node = q.popleft()

            if not node:
                if q:
                    q.append(None)
                lvOrder.append(currentOrder)
                currentOrder = []
            else:
                currentOrder.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return lvOrder[::-1]
        