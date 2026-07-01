class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(matrix, target)

        m = len(matrix)     #number of rows
        n = len(matrix[0])  #number of columns

        # we can do coarse searching and then a fine searching in a particular row
        t = 0       #starting row index. This is the same as the left pointer
        b = m - 1   #ending row index. Same as the right index pointer 

        while t <= b:               #while the l and r pointers don't cross. i.e. there's still rows to search
            row_mid = (b + t)//2        #the middle row to search 

            if target < min(matrix[row_mid]):   #if the target val is smaller than the minimum of the mid row
                b = row_mid - 1                 #then move the right pointer accordingly
            elif target > max(matrix[row_mid]): #or if the val is larger than the max value in the middle row
                t = row_mid + 1                 #move the left pointer
            else:                           #otherwise the target is (possibly) in the mid row
                break                       #so break out of the while loop

        if not t <= b:             #if the pointers crossed each other
            return False           #then the value isn't in the matrix

        #now we'll search the single candidate row that may contain the value. Same exact process as above
        l = 0                       
        r = len(matrix[row_mid]) - 1

        while l <= r:
            m = (l + r)//2

            if target < matrix[row_mid][m]:
                r = m - 1
            elif target > matrix[row_mid][m]:
                l = m + 1
            else:
                break
        
        return matrix[row_mid][m] == target     #if the candidate value matches the target then return True. Else False
        


