# Max Depth of BT logic but you have to consider 0 cases also
# Do a dry run of this case [2,null,3,null,4,null,5,null,6], ans = 5 [THINK!!]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        leftH = self.minDepth(root.left) 
        rightH = self.minDepth(root.right)

        if leftH == 0 and rightH != 0:
            return 1+rightH
        elif leftH != 0 and rightH == 0:
            return 1+leftH
        else:
            return 1+min(leftH, rightH)
        