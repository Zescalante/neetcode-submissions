class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #initialize maps for rows, cols, and 3x3 arrays to check each value against
        row_dict, col_dict, sub_dict = defaultdict(list), defaultdict(list), defaultdict(list)        
        for row in range(len(board)):   #loop through all indices
            for col in range(len(board)):
                # if the current elemnt is a period, we just ignore 
                if board[row][col] == '.':
                    continue
                # if the el has already been seen in the given row, col or subarry, then False
                if board[row][col] in row_dict[row] or \
                board[row][col] in col_dict[col] or \
                board[row][col] in sub_dict[3*(row // 3) + (col // 3)]:
                    return False
                # otherwise we have an unseen elements so add it to all hashmaps
                row_dict[row].append(board[row][col])
                col_dict[col].append(board[row][col])
                sub_dict[3*(row // 3) + (col // 3)].append(board[row][col])
        
        return True 

# time: O(n^2)
# space: O(n^2)
            








# time: O(n^2)
# space: O(n^2)