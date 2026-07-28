class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # search until we find an island (1), flips all ones to zeros, increment island count

        islands = 0

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


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)

        return islands