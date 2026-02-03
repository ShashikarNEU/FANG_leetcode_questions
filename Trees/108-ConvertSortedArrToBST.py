# Observe the test cases, you will find that BST always starts from the middle node
# for the left and right sub trees, recursively call the middle from the left sides and right sides of the array
# Termination codn is when the left > right return None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums):
        def convertArrToBST(left, right):
            if left > right:
                return None
            middle = (left+right)//2
            root = TreeNode(nums[middle])
            root.left = convertArrToBST(left, middle-1)
            root.right = convertArrToBST(middle+1, right)
            return root
        return convertArrToBST(0,len(nums)-1)