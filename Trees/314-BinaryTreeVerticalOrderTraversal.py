# Use BFS(Level Order) here
# start from root at 0 and when going left -1, right +1 and use (node, col_count) in queue
# for storing, use hashMap (count_col, node.val-list)
# instead of sorting, you can use a max_col, min_col variable and use a loop from min_col to max_col

from collections import defaultdict, deque
class Solution:
    def verticalOrder(self, root):
      hashMap = defaultdict(list)

      queue = deque()
      queue.append((root, 0))
      max_col = float('-inf')
      min_col = float('inf')

      while queue:
         node, col = queue.popleft()

         max_col = max(max_col, col)
         min_col = min(min_col, col)

         hashMap[col].append(node)

         if node.left:
            queue.append((node.left, col-1))
         if node.right:
            queue.append((node.right, col+1))
      
      res = []
      for i in range(min_col, max_col+1):
         res.append(hashMap[i])
      
      return res
         




        