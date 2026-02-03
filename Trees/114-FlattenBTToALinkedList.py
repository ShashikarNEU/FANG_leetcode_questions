# Tricky Question, should be hard not meduim

class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return root
            
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)

            if leftTail:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            
            # if rightTail is null, then leftTail will be returned. if leftTail is null then root will be returned
            last = rightTail or leftTail or root 
            
            return last
        
        dfs(root)

# The Core Idea
# The function uses a post-order traversal (Left, Right, Root) approach. The key insight is that the dfs helper function does two things:

# It flattens the subtree it's given.

# It returns the tail node (the very last node) of the flattened list it just created.

# This tail node is crucial because it tells the parent node where to "stitch" the next part of the tree.

# Let's trace the execution with your input tree.

# Initial Tree:

#       1
#      / \
#     2   5
#    / \   \
#   3   4   6
# Step-by-Step Execution Trace
# The process dives deep into the recursion first, and the "stitching" happens as the calls return.

# 1. Dive to the Leftmost Leaf
# flatten calls dfs(1).

# dfs(1) calls dfs(2) on its left child.

# dfs(2) calls dfs(3) on its left child.

# dfs(3) is a leaf. It calls dfs(null) for its left and right children. Both return null.

# Inside dfs(3), leftTail is null and rightTail is null.

# The if condition is skipped.

# last becomes node 3.

# dfs(3) returns 3.

# 2. Process Node 2's Subtree
# We're back in dfs(2). The call to dfs(3) returned 3. So, leftTail is now node 3.

# dfs(2) now calls dfs(4) on its right child.

# Like node 3, dfs(4) is a leaf. It does its work and returns 4.

# Now, back in dfs(2):

# leftTail = 3

# rightTail = 4

# The if leftTail: condition is true. This is where the magic happens for the subtree of 2:

# leftTail.right = root.right becomes 3.right = 4. This connects the end of the flattened left side to the beginning of the right side.

# root.right = root.left becomes 2.right = 3. This moves the entire flattened left subtree to be the right child of 2.

# root.left = None becomes 2.left = None.

# The subtree at 2 now looks like a list: 2 -> 3 -> 4.

# last = rightTail or leftTail or root evaluates to 4.

# dfs(2) returns 4 (the new tail of its flattened subtree).

# Tree State After dfs(2) Finishes:

#       1
#      / \
#     2   5
#      \   \
#       3   6
#        \
#         4
# 3. Dive to the Rightmost Leaf
# We're back in the initial dfs(1) call. The call to dfs(2) returned 4. So, leftTail is now node 4.

# dfs(1) now calls dfs(5) on its right child.

# dfs(5) calls dfs(null) for its left child (returns null).

# dfs(5) calls dfs(6) for its right child.

# dfs(6) is a leaf. It does its work and returns 6.

# Back in dfs(5):

# leftTail = null

# rightTail = 6

# The if leftTail: condition is false, so no stitching happens here.

# last becomes 6.

# dfs(5) returns 6.

# 4. Final Stitching at the Root (Node 1)
# We're finally back at the top level, in dfs(1):

# leftTail = 4 (the tail of the completely flattened 2 -> 3 -> 4 list).

# rightTail = 6 (the tail of the 5 -> 6 list).

# The if leftTail: condition is true. The final stitching occurs:

# leftTail.right = root.right becomes 4.right = 5. This connects the end of the entire flattened left side (4) to the beginning of the original right side (5).

# root.right = root.left becomes 1.right = 2. This moves the entire flattened left subtree to be the right child of the root 1.

# root.left = None becomes 1.left = None.

# Final Result:

# The root (node 1) has been modified in-place to become the head of this flattened list:

# 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Or, more accurately, with the nulls shown:

# 1 -> null, 2 -> null, 3 -> null, 4 -> null, 5 -> null, 6

