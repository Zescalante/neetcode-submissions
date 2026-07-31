from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # DFS starting from every 'O' on border of grid
        rows, cols = len(board), len(board[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(i, j):
            if min(i, j) < 0 or (i > rows - 1) or (j > cols - 1) or \
            board[i][j] == 'X' or board[i][j] == '*':
                return 
            
            board[i][j] = '*'

            for d in directions:
                dfs(i + d[0], j + d[1])
        
        # traverse the borders
        for r in range(rows): #left and right columns
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols): #top and bottom rows
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '*':
                    board[r][c] = 'O'


            
        # q = deque()
        # # find indices of 'O' to kickstart capturing
        # for row in range(rows):
        #     for col in range(cols):
        #         if baord[row][col] == 'O':
        #             q.append([row, col])

        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()
        #         for d in directions:
        #             new_r, new_c = r + d[0], c + d[1]

        #             if (0 <= new_r < rows) and  (0 <= new_c < cols) and \
        #             board

        #                 board[new_r][new_c] = 'X'


        
# time: O(m*n)
# space: O(m*n)