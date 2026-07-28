class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0]) #always get dimensions

        # search until we find an island (1), flips all ones to zeros, increment island count
        def dfs(r, c):

            #boundary and water cases
            if (min(r, c) < 0) or (r > rows - 1) or (c > cols - 1) or \
            grid[r][c] == '0':
                return
            
            if grid[r][c] == '1':
                grid[r][c] = '0'
                dfs(r + 1, c) 
                dfs(r - 1, c) 
                dfs(r, c + 1) 
                dfs(r, c - 1) 

        islands = 0 #initialize island counter
        
        for row in range(rows):     #search through every spot in the grid
            for col in range(cols):
                if grid[row][col] == '1':   #if we found land 
                    islands += 1            #then we increment counter here, and then dfs
                    dfs(row, col)           #to switch island ones to zeros

        return islands

# time: O(n*m)
# space: O(n*m)