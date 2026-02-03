# Use BFS(Lv Order) here
# On first glance, it seems easy but it's a bit tricky
# DONT LINK NODES WHEN ENQUEUEING, INSTEAD DO IT WHEN POPPING FROM QUEUE
# HERE, we need to take care of levels(we can't link nodes in different levels)
# When changing levels, make prev = None

# When popping the nodes, link them. if null, set prev to None. if prev is None then, prev = node then if not prev.next=node and set prev = node. All nodes will be linked [THINK, use a example for understanding easily]
# Prereq - Lv Order, Linked List pointer problems

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
        