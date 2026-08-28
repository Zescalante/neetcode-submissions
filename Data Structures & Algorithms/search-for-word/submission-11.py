class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])  #board dimensions 
        directions = [[-1,0],[1,0],[0,1],[0,-1]] #four directions to step in 
        seen = set() #store visited index pairs

        def dfs(i, j, w): #(i, j) grid indices; w = word index
            if w == len(word): #base case
                return True
                
            if (i, j) in seen or min(i, j) < 0 or \
            i > rows - 1 or j > cols - 1 or \
            board[i][j] != word[w]:
                return False

            seen.add((i, j)) # add (i, j) to visited index set

            for d in directions:
                if dfs(i + d[0], j + d[1], w + 1):
                    return True
        
            seen.remove((i, j))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
    
# time: O(m*4^n); m = #cells in the board, n=size of word
# space: O(n)