class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        #edge case if matrix is single element
        if len(matrix) == 1:
            return matrix

        n = len(matrix)   #get dimensions. Square matrix

        #switch rows vertically
        for idx in range(n // 2):
            matrix[idx], matrix[n - 1 - idx] = matrix[n - 1 - idx], matrix[idx]

        # flip indices (i ,j) -> (j, i). Only need top right matrix indices.
        for i in range(n):
            for j in range(n):
                if j > i:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# time: O(n^2) so we have to work with each element
# space: O(1)