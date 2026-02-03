# https://www.youtube.com/watch?v=_-QHfMDde90

# Here we follow a recursive dfs in the BT. when we encounter p and q, return it
# while retuning, if we get non none value and none value from left and right rec calls
# just return non none value above. eventually, we will receive p and q on left and right for a node.
# return that node(This is your answer)

# we return the non-null value because after finding p or q, we have to peserve/return it before. 
# Case1: if p is found, not q, return p up
# Case2: if q is found, not p, return q up
# Case3: if p and q is found, then root is the answer, return it up[this will lead to case1 or 2 recursively and we will get root as the answer]

# Do a dry run with example to understand this!!
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left and not right:
            return None
        elif not right and left:
            return left
        elif not left and right:
            return right
        elif left and right:
            return root