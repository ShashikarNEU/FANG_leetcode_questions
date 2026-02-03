# Main Logic
# do dfs in the tree and form a parent table in a dict
# then do lv order with a twist(Also check in the parent in addition to left and right child)

# Treat this question as a BFS Graph question
# Do visited logic inside NOT IMMEDIATELY AFTER popping the node
# check k after popping, do visited logic exactly LIKE BFS

# Let the code run untill the QUEUE IS EMPTY anyways the TC will be n and SC is also n

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        parentTable = defaultdict(TreeNode)

        def recordParents(root):
            nonlocal parentTable
            if not root:
                return
            if root.left:
                parentTable[root.left] = root
            if root.right:
                parentTable[root.right] = root

            recordParents(root.left)
            recordParents(root.right)
        
        recordParents(root)

        queue = deque()

        queue.append((target,0))
        res = []
        visited = set()
        visited.add(target)
        
        while queue:
            node, lv = queue.popleft()

            if lv == k:
                res.append(node.val)
            
            # Check parent
            if node in parentTable and parentTable[node] not in visited:
                visited.add(parentTable[node])
                queue.append((parentTable[node], lv+1))
                
            # Check left children
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append((node.left, lv+1))
            
            # Check right children
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append((node.right, lv+1))
               
        return res