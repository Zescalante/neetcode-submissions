class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or \
            obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        prev_row = [0]*(cols + 1)
        prev_row[cols - 1] = 1 #set 1 at target (bottom right)

        for r in range(rows - 1, -1 , -1):
            curr_row = [0]*cols
            # curr_row[-1] = 1
            for c in range(cols - 1, -1, -1):
                
                if obstacleGrid[r][c] == 1:
                    curr_row[c] = 0 
                    continue 
                # elif prev_row[-1] == 1:


                curr_row[c] = (curr_row[c + 1] if c + 1 < cols else 0) + prev_row[c]
            
            prev_row = curr_row

        return prev_row[0]