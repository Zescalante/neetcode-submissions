class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # sorted in non-decreasing order -> binary search
        # binary search on the rows, then binary search on the single row (maybe) containing target

        t, b = 0, rows - 1 #top and bottom row pointers

        while t <= b:   #check all rows, including when t == b
            mid = (t + b) // 2
            if matrix[mid][0] > target: #if the smallest el in row is still larger than target
                b = mid - 1 #move bottom pointer up, and we search top half

            elif matrix[mid][-1] < target: #if the largest el in row is still smaller than target
                t = mid + 1 #move top pointer down, and we search lower half

            else: #otherwise the target is somewhere in the current row
                break

        l, r = 0, cols - 1 #left and right pointers for row

        target_row = matrix[mid]

        while l <= r:   #check all els
            mid = (l + r) // 2
            if target_row[mid] > target: #if target smaller than mid element, then search left half
                r = mid - 1

            elif target_row[mid] < target: #if target larger than mid element, then search right half
                l = mid + 1

            else: #otherwise we found target
                return True

        return False #if we get here, then target was not in the matrix

# time: O(log(m*n)) = O(logm + logn)
# space: O(1)