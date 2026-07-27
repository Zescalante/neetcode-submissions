class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])
        positions = [[0,1],[1,0],[0,-1],[-1,0]] 
        visited = set()

        def backtracking(i , j, w):

            if i < 0 or i > rows - 1 or \
                j < 0 or j > cols - 1 or \
                board[i][j] != word[w] or \
                (i, j) in visited:
                return False

            visited.add((i, j)) 

            # what do if the character is in the word?
            # if board[i][j] == word[w]:
            if w == len(word) - 1:
                return True
            else:
                w += 1
                for p in positions:
                    new_row = i + p[0]
                    new_col = j + p[1]

                    if backtracking(new_row, new_col, w):
                        return True

                visited.remove((i,j))
                return False

        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0):
                    return True
        
        return False