from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = cols = len(grid) #it's a square matrix
        visits = set()   #stores the previously-visited nodes, so we don't double-check
        queue = deque()  #store the current level's nodes to check

        if grid[0][0] == 1: #if the first value is 1, we can't start the process!
            return -1

        visits.add((0,0))    # add the top left cell, since that's where we're starting
        queue.append((0,0))      # add the first element to the queue so we can check it in bfs
        
        #eight directions to search in, since we can go diagonally
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        def bfs(arr):

            path = 1 #initialize shortest path counter at 1, since we checked (0,0)

            while queue:                #while the queue in no empty
                for _ in range(len(queue)): #step through each stored coordinate in the queue
                    r, c = queue.popleft()  #extract the indices

                    if r == rows - 1 and c == cols - 1: #if we're at the bottom right  
                        return path     #then we've hit the destination. Return the path
                    
                    for dr, dc in directions:   #otherwise, we'll step in all 8 directions
                        #if we've hit the boundary, or already seen this coordinate, or the element is 1
                        if (min(r + dr, c + dc) < 0) or (r + dr == rows) or \
                        ((r + dr, c + dc) in visits) or \
                        (c + dc == cols) or (arr[r + dr][c + dc] == 1):
                            continue    #continue to the next directions, since this is can't be included

                        queue.append((r + dr, c + dc))  #if checks are passed, add coordinate to the queue
                        visits.add((r + dr, c + dc))    #and to the visits set, so we don't check again

                path += 1   #increment path by 1 to after each level is checked

            return -1       #if we didn't hit the end successfully, return -1

        return bfs(grid)    #run bfs on the grid