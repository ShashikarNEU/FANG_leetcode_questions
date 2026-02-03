# Do a dry run and understand the question first

# Understand that right children have no children so, just f(root.left) call is enough
# Go to the last left most node and apply pointer changes
# We should apply pointer changes when root has left and right child(root.left is the new root) [For the leftmost child]
# root.left.right = root
# root.left.left = root.right
# root.left = None
# root.right = None
# Write a base codn for the new root(if not root.left and not root.right return root) and return it up the recursive chain

# https://www.youtube.com/watch?v=JjaJQi77984 [Reference video!!]
class Solution:
    def upsideDownBinaryTree(self, root):
        def upsideBT(root):
            if not root:
                return root

            if not root.left and not root.right:
                return root
            
            new_root = upsideBT(root.left)
            
            root.left.right = root
            root.left.left = root.right
            root.left = None
            root.right = None

            return new_root

        return upsideBT(root)
