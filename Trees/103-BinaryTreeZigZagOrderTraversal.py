# Same logic as Lv order
# but use a flag for reversing alternate currentOrders(or you can use count here)

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        q = deque()
        q.append(root)
        q.append(None)

        currentOrder = []
        zigZagOrder = []

        zigZag_flag = True

        while q:
            node = q.popleft()

            if not node:
                if q:
                    q.append(None)
                if not zigZag_flag:
                    currentOrder = currentOrder[::-1]
                zigZagOrder.append(currentOrder)
                zigZag_flag = not zigZag_flag
                currentOrder = []
                continue
            
            currentOrder.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return zigZagOrder
                    
                
