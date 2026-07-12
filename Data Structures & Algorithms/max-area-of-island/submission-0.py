class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0 
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows, cols = len(grid), len(grid[0]) 

        #this time we need to track the max size of an island
        max_size = 0 
    
        def dfs(r, c):

            if (min(r, c) < 0) or \
                (r == rows) or (c == cols) or \
                (grid[r][c] == 0):
                return 0

            area = 1
            grid[r][c] = 0

            for dr, dc in directions:
                area += dfs(r + dr, c + dc)

            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:

                    # size = 1
                    max_size = max(dfs(i, j), max_size)

        return max_size

        