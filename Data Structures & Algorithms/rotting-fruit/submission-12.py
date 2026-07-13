from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])    #get the number of rows and cols

        queue = deque()     #initialize the queue to add rotten fruit indices to

        directions = [[-1,0],[1,0],[0,-1],[0,1]]    #we're searching in 4 directions 

        minutes = 0         #initialize minutes passed
        fresh_count = 0     #and the number of fresh fruit left in the grid

        for i in range(rows):           #step through each spot in the grid
            for j in range(cols):
                if grid[i][j] == 2:     #if we have a rotten fruit
                    queue.append((i,j)) #add the location to the queue
                elif grid[i][j] == 1:   #if we have a fresh fruit
                    fresh_count += 1    #increment the fresh counter 
        
        if fresh_count == 0:            #now check if there's any fresh fruit to begin with. If not
            return 0                    #then return 0 since no time needed 

        while queue and fresh_count > 0:    #else, while there's rotten fruit in the grid and fresh fruit left...
            for _ in range(len(queue)):     #step through each location in the queue
                r, c = queue.popleft()      #get the indices
                
                for dr, dc in directions:   #and step in the 4 directions

                    #if we're out of bounds, or we're not at a fresh fruit
                    if (min(r + dr, c + dc) < 0) or \
                    (r + dr == rows) or (c + dc == cols) or \
                    grid[r + dr][c + dc] != 1:      
                        continue                    #then move to next spot

                    queue.append((r + dr, c + dc))  #if conditions met, we have a fresh fruit, so add queue

                    grid[r + dr][c + dc] = 2    #turn fruit rotten
                    fresh_count -= 1            #and decrement the fresh counter

            minutes += 1    #after each pass of the queue, one time step has passed, so increment by 1

        return minutes if fresh_count == 0 else -1  #after loop, return the time passed if no more fresh, or -1 if we couldn't reach them all
                     
# time: O(n*m)
# space: O(n*m)