# Same logic as 116 Question(no change)
# Refer that first
# PreReq - lvOrder, LinkedList Pointer problems
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:
    def connect(self, root):
        queue = deque()
        # levelOrder = []
        # currentOrder = []
        if not root:
            return root
        queue.append(root)
        queue.append(None)
        prev = None
        while queue:
            node = queue.popleft()
            if not node:
                if queue:
                    queue.append(None)
                # levelOrder.append(currentOrder)
                # currentOrder = []
                prev = None
            else:
                if not prev:
                    prev = node
                else:
                    prev.next = node
                    prev = node
                # currentOrder.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
        