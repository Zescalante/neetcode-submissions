class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:        #if no input grid   
            return 0        #then no max island area! Return 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] #directions to step in for recursion
        rows, cols = len(grid), len(grid[0])    #size of the input grid

        #this time we need to track the max size of an island
        max_size = 0 
    
        def dfs(r, c):
            
            #if we're out of bounds or hit a 0.....
            if (min(r, c) < 0) or \
                (r == rows) or (c == cols) or \
                (grid[r][c] == 0):
                return 0        #then zero contributino to the island area

            area = 1        #else, initialize the area for this island
            grid[r][c] = 0  #set the pixel location to zero so it won't re-search

            for dr, dc in directions:       #step into the other directions 
                area += dfs(r + dr, c + dc) #and add area contributions 

            return area #return the area island at the end of dfs
        
        for i in range(rows):       #step through each location in the grid
            for j in range(cols):
                if grid[i][j] == 1: #if we find land
                    max_size = max(dfs(i, j), max_size) #recurse, and store the new maximum island area

        return max_size #return the max island area!

# time: O(n*m)
# space: O(n*m)

        