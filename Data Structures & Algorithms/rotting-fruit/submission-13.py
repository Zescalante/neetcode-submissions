from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS. Start from each rotted fruit. Change adjenct fresh to rotten.
        # iterate through all points? Or just the rotten fruit?
        directions = [[1,0],[0,1],[-1,-0],[0,-1]]
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        fresh_count = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0
        if not rotten and fresh_count > 0:
            return -1

        while rotten and fresh_count > 0:
            for i in range(len(rotten)):
                orange = rotten.popleft()
                for d in directions:
                    new_r = orange[0] + d[0]
                    new_c = orange[1] + d[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        rotten.append((new_r,new_c))
                        fresh_count -= 1
            time += 1

        return time if fresh_count == 0 else -1



# time: O(m*n)
# space: O(m*n)