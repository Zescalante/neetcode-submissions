class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])    #get the size of the grid

        def dfs(r, c):      #dfs helper!

            #check if out of grid bounds or if hit '0'.
            if (min(r, c) < 0) or \
            (r == rows) or (c == cols) or \
            (grid[r][c] == '0'):
                return          #exit call immediately if conditions met

            grid[r][c] = '0'    #otherwise, set the value to '0' so we don't revisit

            dfs(r + 1, c)       #usual stepping in four directions
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return      #and just exit at the end

        islands = 0     #initialize island counter
        for i in range(rows):       #loop through rows
            for j in range(cols):   #and through columns
                if grid[i][j] == '1':   #if we hit '1' we have an island
                    islands += 1        #so increment the counter
                    dfs(i, j)           #and enter dfs to mark the island as '0'


        return islands      #at the end, return the number of islands!

# time: O(n*m)
# space: O(n*m)
