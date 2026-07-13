from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = cols = len(grid) #it's a square matrix
        visits = set() #stores the previously-visited nodes
        queue = deque()

        if grid[0][0] == 1:
            return -1

        visits.add((0,0))    #add the top left cell, since that's where we're starting
        queue.append((0,0))      #add the first element to the queue, to check
        
        #eight directions to search in, since we can go diagonally
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        def bfs(arr):

            path = 1 #initialize shortest path counter

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if r == rows - 1 and c == cols - 1: #if we're at the bottom right  
                        return path     #then we've hit the destination. Return the path
                    
                    for dr, dc in directions:
                        if (min(r + dr, c + dc) < 0) or (r + dr == rows) or \
                        ((r + dr, c + dc) in visits) or \
                        (c + dc == cols) or (arr[r + dr][c + dc] == 1):
                            continue

                        queue.append((r + dr, c + dc))
                        visits.add((r + dr, c + dc))

                path += 1

            return -1 

        return bfs(grid)