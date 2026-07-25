class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0]) #get array size

        top, left = 0, 0 #indices to increment
        bottom, right = n - 1, m - 1 #indices to decrement

        res = []
        # want to be squeezing the array indices from both sides
        # while top <= n and bottom >= 0 and left <= m and right >= 0:
        # while top <= bottom and left <= right:

        #     res += matrix[top][left:right + 1]    #top row
        #     res +=  matrix[top:bottom + 1][right]  #right column   

        #     top += 1
        #     right -= 1

        #     res += matrix[bottom][left:right + 1:-1]    #bottom row
        #     res += matrix[top:bottom + 1:-1][left]      #left column

        #     bottom -= 1
        #     left += 1
        while top <= bottom and left <= right:

            # top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
            # bottom row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
            # left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res




