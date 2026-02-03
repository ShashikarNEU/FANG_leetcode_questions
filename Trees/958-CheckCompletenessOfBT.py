# Logic
# You will get that we have to use lv order after reading it
# but we don't have to find the height or last lv seperately and check null then, node
# we can apply a general logic which works in all levels, if a node is null in lv2, after that if we encounter
# any non null node somewhere else. return False. same logic for last level

# Realize this and this question is over

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque


class Solution:
    def isCompleteTree(self, root) -> bool:
        queue = deque()

        queue.append(root)
        nullFound = False

        while queue:
            node = queue.popleft()

            if nullFound and node.left:
                return False
            elif node.left:
                queue.append(node.left)
            else:
                nullFound = True

            if nullFound and node.right:
                return False
            elif node.right:
                queue.append(node.right)
            else:
                nullFound = True
        
        return True





        