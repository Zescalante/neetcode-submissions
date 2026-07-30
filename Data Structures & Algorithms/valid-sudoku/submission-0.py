class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # hash set?
        # store (i,j) keys with element value?
        row_dict, col_dict, sub_dict = defaultdict(list), defaultdict(list), defaultdict(list)        
        # seen = set()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] in row_dict[row] or \
                board[row][col] in col_dict[col] or \
                board[row][col] in sub_dict[3*(row // 3) + (col // 3)]:
                    return False
                elif board[row][col] == '.':
                    continue
                row_dict[row].append(board[row][col])
                col_dict[col].append(board[row][col])
                sub_dict[3*(row // 3) + (col // 3)].append(board[row][col])
        
        return True 

        print(row_dict)
        print(col_dict)
        print(sub_dict)
            








# time: O(n^2)
# space: O(n^2)