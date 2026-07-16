# BOTTOM-UP 

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])    #get size of grid

        #edge case. If there's an obstacle in the start or ending spot, then no possible paths
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        prev_row = [0]*(cols + 1)   #initialize a previous row with zeros. Size 1 greater than grid cols
        prev_row[cols - 1] = 1 #set 1 at target index (bottom right)

        for r in range(rows - 1, -1 , -1):      #step through rows from bottom to top
            curr_row = [0]*cols                 #set a current row with zeros
            for c in range(cols - 1, -1, -1):   #step through columns from right to left
                if obstacleGrid[r][c] == 1:     #if there's an obstacle at this index
                    curr_row[c] = 0             #then set 0 in current row locations, since no possible paths through there
                    continue                    #and break out of this for loop, to next row

                #otherwise, update the value at (r,c). If we're out of bounds in columns, don't include that value
                curr_row[c] = (curr_row[c + 1] if c + 1 < cols else 0) + prev_row[c]
            
            prev_row = curr_row     #set new previous row

        return prev_row[0]          #the solution is at index 0 of final previous row

        # time: O(n*m)
        # space: O(n)