from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # visits = set()
        queue = deque()

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        minutes = 0 
        fresh_count = 0 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        # if not queue:
        #     return -1

        while queue and fresh_count > 0:
            fruit_rotted = False
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
    
                    if (min(r + dr, c + dc) < 0) or \
                    (r + dr == rows) or (c + dc == cols):
                    # ((r + dr, c + dc) in visits) or \
                    # grid[r + dr][c + dc] == 2:
                        continue   

                    if grid[r + dr][c + dc] == 1:
                        # visits.add((r + dr, c + dc))
                        queue.append((r + dr, c + dc))

                        grid[r + dr][c + dc] = 2
                        fresh_count -= 1
                        fruit_rotted = True
                        # minutes += 1
            if fruit_rotted:
                minutes += 1




        return minutes if fresh_count == 0 else -1
                     
            