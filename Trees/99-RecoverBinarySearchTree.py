# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def recoverTreeSub(root):
            if not root:
                return
            
            recoverTreeSub(root.left)
            arr.append(root)
            recoverTreeSub(root.right)
        
        recoverTreeSub(root)
        first = None
        second = None
        for i in range(len(arr)):
            node = TreeNode(float('-inf')) if i == 0 else arr[i-1]

            if node.val >= arr[i].val:
                if first is None:
                    first = arr[i-1]
                second = arr[i]

        first.val, second.val = second.val, first.val