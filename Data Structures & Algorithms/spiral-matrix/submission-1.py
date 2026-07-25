class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0]) #get array size

        top, left = 0, 0 #indices to increment
        bottom, right = n - 1, m - 1 #indices to decrement

        res = []    #need to store the ordered valeus

        #outer check
        while top <= bottom and left <= right:

            # top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # bottom row
            #need to check a second time if top is <= bottom
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # left column
            #same here for left <= right
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

# time: O(n*m)
# space: O(n*m)




