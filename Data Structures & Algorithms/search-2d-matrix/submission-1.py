class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        top, bottom = 0, m - 1

        while top <= bottom:
            middle = (top + bottom) // 2

            if target < matrix[middle][0]:
                bottom = middle - 1

            elif target > matrix[middle][-1]:
                top = middle + 1
            else:
                break

        if not top <= bottom:
            False

        l, r = 0, n - 1
        arr = matrix[middle]

        while l <= r:
            m = (l + r) // 2
            if target < arr[m]:
                r = m - 1
            elif target > arr[m]:
                l = m + 1
            else: 
                break

        return target == arr[m]
        



            