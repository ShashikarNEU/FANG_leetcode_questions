from collections import defaultdict
from typing import List

# Here we take every island in a hashMap
# have unique_id -> size in a hashMap
# Then, after visiting a island, mark it with it's unique_id to identify it
# Finally, search for zeros and do 1+sum(in all 4 direction islands) -> for every zero and take max of that!!

# https://www.youtube.com/watch?v=pq61VNqXGvA

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(row, col, unique_id):
            if row < 0 or col < 0 or row >= ROW or col >= COL or grid[row][col] == unique_id or grid[row][col] == 0:
                return 0
            
            grid[row][col] = unique_id
            area = 1

            for r,c in directions:
                area += dfs(row+r, col+c, unique_id)
            return area
        
        hashMap = defaultdict(int)
        unique_id = 2
        max_area = float('-inf')
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    area = dfs(r, c, unique_id)
                    hashMap[unique_id] = area
                    max_area = max(max_area, area)
                    unique_id += 1
        
        # We are declaring max area before because what if there are no zeros, max area without flipping zeros will be the answer
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    unique_id_set = set()
                    large_island_area = 1
                    for row,col in directions:
                        nr, nc = row+r, col+c
                        if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                            continue
                        if grid[nr][nc] != 0 and grid[nr][nc] not in unique_id_set:
                            unique_id_set.add(grid[nr][nc])
                            large_island_area += hashMap[grid[nr][nc]]
                    
                    max_area = max(max_area, large_island_area)
        
        return max_area



        



        