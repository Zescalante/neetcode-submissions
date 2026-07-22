# DFS. MEMOIZED?
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()
        directions = [[0,1], [1,0], [0,-1],[-1,0]]

        def dfs(row, col, cache):
            
            if row < 0 or col < 0 or row >= rows or \
            col >= cols or (row, col) in cache:
                return 

            # if (row, col) in cache:
            #     return cache((row, col))

            cache.add((row, col))

            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if 0<= new_row < rows and 0<= new_col < cols and heights[new_row][new_col] >= heights[row][col]:
                    dfs(new_row, new_col, cache)


        pacific_coords = [[0, x] for x in range(cols)] +[[y, 0] for y in range(rows)]
        atlantic_coords = [[rows - 1, x] for x in range(cols)] +[[y, cols - 1] for y in range(rows)]

        for p in pacific_coords:
            dfs(p[0], p[1], pacific)
        for a in atlantic_coords:
            dfs(a[0], a[1], atlantic)

        res = []

        for p in pacific:
            if p in atlantic:
                res.append(p)

        return res