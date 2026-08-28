class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])  #board dimensions 
        directions = [[-1,0],[1,0],[0,1],[0,-1]] #four directions to step in 
        seen = set() #store visited index pairs

        def dfs(i, j, w): #(i, j) grid indices; w = word index
            if w == len(word): #base case. If we make it to end of the word,
                return True #then we found a match, so True
            #base cases if OOB of indices visited or characters don't match
            if (i, j) in seen or min(i, j) < 0 or \
            i > rows - 1 or j > cols - 1 or\
            board[i][j] != word[w]:
                return False

            seen.add((i, j)) # add (i, j) to visited index set

            for d in directions:    #search in the four directions
                if dfs(i + d[0], j + d[1], w + 1):
                    return True #if the dfs call returns True, then propagate
        
            seen.remove((i, j)) #after, remove the index pair so we can visit later
            return False    #return False, since we haven't found a match

        for r in range(rows):   #have to start from every cell, one at a time
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
    
# time: O(m*4^n); m = #cells in the board, n=size of word
# space: O(n)