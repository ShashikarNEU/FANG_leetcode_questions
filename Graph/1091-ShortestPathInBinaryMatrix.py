# Shortest path -> Think of BFS not DFS(backtracking, expensive)
# Apply normal matrix BFS with dist, when it reaches (n-1,n-1) first that's the shortest path
# return dist there. else return -1

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

        queue = deque()
        visited = set()

        if grid[0][0] == 1:
            return -1
        
        # row, col, dist
        queue.append((0,0,1))

        while queue:
            row, col, dist = queue.popleft()

            if row == ROW-1 and col == COL-1:
                return dist

            for r,c in directions:
                nr, nc = row+r, col+c

                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or (nr,nc) in visited or grid[nr][nc] == 1:
                    continue
                
                visited.add((nr,nc))
                queue.append((nr,nc,dist+1))
        
        return -1



        