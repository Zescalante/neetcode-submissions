class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = cols = len(board) #square dimensions
        row_dict, col_dict, sub_dict = defaultdict(set), defaultdict(set), defaultdict(set)  #dict to store seen numbers

        for row in range(rows):
            for col in range(cols):
                val = board[row][col]
                if val == '.':
                    continue
                elif val not in row_dict[row] and \
                val not in col_dict[col] and \
                val not in sub_dict[3*(row // 3) + (col // 3)]:
                    row_dict[row].add(val)
                    col_dict[col].add(val)
                    sub_dict[3*(row // 3) + (col // 3)].add(val)
                else:
                    return False
        return True




# time: O(n^2)
# space: O(n^2)