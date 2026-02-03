# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Logic
# Really similar to 938(Recursion visual)

# follow postorder here, after visiting the full subtree, you come to the root of that sub tree
# perfect for this question
# return [sum, count](return 2 things here)
# then from left and right sub tree, add counts and sums. then, return that(Visualize the recursion pls)
# Do Dry Run and visualize the recursion
class Solution:
    def averageOfSubtree(self, root) -> int:
        res_count = 0

        def avg_subtree(root):
            nonlocal res_count
            if not root:
                return 0,0
            
            left_sum, left_count = avg_subtree(root.left)
            right_sum, right_count = avg_subtree(root.right)


            total_sum = root.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            avg_val = (total_sum//total_count)

            if avg_val == root.val:
                res_count+=1
            
            return total_sum, total_count
        
        avg_subtree(root)
        return res_count
