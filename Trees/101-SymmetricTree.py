# Follow up to same tree question(same code but just opposite traversal)
class Solution:
    def isSymmetric(self, root) -> bool:
        def mirrorTrees(p,q):
            if not p and not q:
                return True
            if not p and q:
                return False
            if p and not q:
                return False
            if p.val != q.val:
                return False
            return mirrorTrees(p.left, q.right) and mirrorTrees(p.right, q.left)

        return mirrorTrees(root.left, root.right)