# Root to leaf path logic
# But when adding stack to the result list, it will add the reference of the stack not the stack itself
# so you have to do stack.copy() and add stack
# THEY MIGHT TEST IN THE INTERVIEW
# This case also happens 3-4 times in backtracking section also
class Solution:
    def pathSum(self, root, targetSum: int):
        stack = []
        result = []
        def sumPath(root):
            if not root:
                return
            stack.append(root.val)
            if not root.left and not root.right:
                if sum(stack) == targetSum:
                    result.append(stack.copy())
            sumPath(root.left)
            sumPath(root.right)
            stack.pop()

        sumPath(root)
        return result