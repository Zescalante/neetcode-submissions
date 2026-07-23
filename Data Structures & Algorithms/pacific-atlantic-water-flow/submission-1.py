class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs; work backwards; sets to store pacific and atlantic visits

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(row, col, visits):

            if row < 0 or row > rows - 1 or \
            col < 0 or col > cols - 1 or (row, col) in visits:
                return 

            visits.add((row, col))

            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and \
                heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, visits)



        res  = []

        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows - 1, c, atl)

        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols - 1, atl)

        for cell in pac:
            if cell in atl:
                res.append(cell)

        return res
