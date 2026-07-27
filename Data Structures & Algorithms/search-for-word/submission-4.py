class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])  #get dimensions
        positions = [[0,1],[1,0],[0,-1],[-1,0]] #define steps
        visited = set()         #initialize set to store explored locations

        #general dfs structure with array idx i,j and word index w
        def backtracking(i , j, w):
            if w == len(word):  #first check if we've hit the end of the word
                return True     #if we have, then success
            
            # if not, check edge cases: out of array, or not correct letter
            # or cell is already visited
            if i < 0 or i > rows - 1 or \
                j < 0 or j > cols - 1 or \
                board[i][j] != word[w] or \
                (i, j) in visited:
                return False

            visited.add((i, j))  #we add the cell to current visited set

            #then take a step in each direction
            for p in positions:
                if backtracking(i + p[0], j + p[1], w + 1):
                    return True     #we return true if valid path found

            # after searching directions, we remove the current cell, for other
            # loop to explore
            visited.remove((i,j))

            return False   #if we get here, then no valid path found, so False

        # in the main function, we explore starting from each cell
        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0): 
                    return True     #if path found, then return True
        
        # If not, return false 
        return False

# time: O(n*m*4^L); n = rows, m = cols, L = size of word
# space: O(L)