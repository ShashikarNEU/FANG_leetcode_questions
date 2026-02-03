# FOLLOW UP TO 257(SAME LOGIC)
# Preorder - Root to leaf paths

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root) -> int:
        stack = []
        result = []

        def sumPath(root):
            if not root:
                return
            stack.append(root.val)
            if not root.left and not root.right:
                #print(stack)
                string = ""
                for s in stack:
                    string += str(s)
                result.append(int(string))
            sumPath(root.left)
            sumPath(root.right)
            stack.pop()

        sumPath(root)
        return sum(result)
