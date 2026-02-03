from collections import deque

# Logic

# In the context of Minimum Knight Moves, you are correct 
# that standard Dynamic Programming (DP) or Backtracking becomes 
# very difficult because the state space theoretically stretches from −∞ to ∞.

# So, use BFS(Think!!)
# it's pretty easy to write the BFS once you realize it
# since, it's -inf to inf, no need for checks  - < 0 or >= n 

# Unoptimized BFS
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [[2,1],[2,-1],[1,2],[-1,2],[-2,1],[-2,-1],[1,-2],[-1,-2]]

        queue = deque()
        visited = set()

        queue.append((0,0,0)) # row,col,moves

        while queue:
            row,col,moves = queue.popleft()

            if row == x and col == y:
                return moves

            for r,c in directions:
                nr,nc = row+r, col+c

                if (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,moves+1))
        
        return -1
  
# Optimizied BFS
# Here, we can consider symmetry but all four quardants are the same
# so, use abs(x) and abs(y) as targets
# but, we need to consider about paths going slightly -ve so, add checks for them in BFS(inside directions loop)

from collections import deque

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)  # symmetry
        
        directions = [(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(1,-2),(-1,-2)]
        queue = deque([(0, 0, 0)])
        visited = {(0, 0)}

        while queue:
            row, col, moves = queue.popleft()
            
            if row == x and col == y:
                return moves

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                
                # bound the search: don't go too far negative (edge cases near origin need -2)
                if (nr, nc) not in visited and nr >= -2 and nc >= -2:
                    visited.add((nr, nc))
                    queue.append((nr, nc, moves + 1))
        
        return -1


        