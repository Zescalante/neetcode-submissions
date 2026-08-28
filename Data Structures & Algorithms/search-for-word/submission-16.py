class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        visited = set()

        def dfs(i, j, w):

            if w == len(word):
                return True
            
            if min(i, j) < 0 or i > rows - 1 or j > cols - 1 or \
            (i,j) in visited or board[i][j] != word[w]:
                return False

            visited.add((i,j))

            for d in directions:
                new_i, new_j = i + d[0], j + d[1]
                if dfs(new_i, new_j, w + 1):
                    return True 

            visited.remove((i,j))
            
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False