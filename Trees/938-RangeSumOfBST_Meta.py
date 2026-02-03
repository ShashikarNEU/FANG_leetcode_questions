# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Reference Video -> https://www.youtube.com/watch?v=dNulwIl2gCI

# Brute Force - Go through every node and check if it's within range and add it to the result
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def rangeSum(root):
            if not root:
                return 0
            res = 0
            if low <= root.val <= high:
                res = root.val
            res += rangeSum(root.left)
            res += rangeSum(root.right)
            return res

        return rangeSum(root)

# Optimal Soln
# 3 cases
# 1. if root.val is bw the range, Explore right and left sub trees get sum from there and return root+f(root.left)+f(root.right)
# 2. if root.val < low, then there is a change that if we go right, root.val will come in within range. so, return f(root.right)
# it will go through the root.right pathway(in recursion) and go to case 1 again.
# 3. if root.val > high, then there is a change that if we go left, root.val will come in within range. so, return f(root.left)
# it will go through the root.left pathway(in recursion) and go to case 1 again.

# Think using a example(DRY RUN)
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        def rangeSum(root):
            if not root:
                return 0
            res = 0
            if low <= root.val <= high:
                res += rangeSum(root.left)
                res += rangeSum(root.right)
                return root.val + res
            elif root.val > high:
                res += rangeSum(root.left)
            elif root.val < low:
                res += rangeSum(root.right) 
            return res

        return rangeSum(root)

# Meta also asks the iterative version of the optimal solution and 2 variants

# Optimal soln - iterative version
# This version is very easy if you know all 3 cases and follow lv order traversal(like, not exactly)
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        stack = []
        res = 0
        stack.append(root)
        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                res += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            elif node.val < low:
                if node.right:
                    stack.append(node.right)
            elif node.val > high:
                if node.left:
                    stack.append(node.left)
        
        return res

# Variant 1 -> same question but find avg instead of sum. Have a count variable
# Iterative version is very easy so, I will try the recursive version
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        count = 0
        def rangeSum(root):
            nonlocal count
            if not root:
                return 0
            res = 0
            if low <= root.val <= high:
                count+=1
                res += rangeSum(root.left)
                res += rangeSum(root.right)
                return root.val + res
            elif root.val > high:
                res += rangeSum(root.left)
            elif root.val < low:
                res += rangeSum(root.right) 
            return res

        return (rangeSum(root)//count)

# or else you can return both [sum, count] in every call instead of global variable(Better)
class Solution:
    def rangeAvgBST(self, root, low: int, high: int) -> float:
        def dfs(node):
            if not node:
                return 0, 0
            if node.val < low:
                return dfs(node.right)
            if node.val > high:
                return dfs(node.left)
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            return node.val + ls + rs, 1 + lc + rc

        total, cnt = dfs(root)
        return total / cnt if cnt else 0.0


# Variant 2



