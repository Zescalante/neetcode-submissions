from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS to by level by level. Start from each rotted fruit. Change adjenct fresh to rotten.
        # iterate through all points? Or just the rotten fruit?
        directions = [[1,0],[0,1],[-1,-0],[0,-1]] #directions to search 
        rows, cols = len(grid), len(grid[0])    #get grid size
        rotten = deque()    #deque because bfs
        fresh_count = 0     #we'll count how many fresh to begin with
        time = 0            #set time to zero

        for r in range(rows):   #first check all cells for fresh and rotten oranges
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:    #if there's no fresh, then no time needed
            return 0
        if not rotten and fresh_count > 0:  #if no rotten, but there's fresh, then not possible
            return -1

        while rotten and fresh_count > 0:   #typical bfs
            for _ in range(len(rotten)):
                orange = rotten.popleft()
                for d in directions:
                    new_r = orange[0] + d[0]
                    new_c = orange[1] + d[1]
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        rotten.append((new_r,new_c))    #this append indices of newly rotten oranges    
                        fresh_count -= 1    #decrement fresh count
            time += 1   #after searching the queue once fully, THEN we increment time

        return time if fresh_count == 0 else -1 #if zero fresh left then return time, else -1

# time: O(m*n)
# space: O(m*n)