# BOTTOM-UP DP

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we're going backwards through the grid. We start from the base case (bottom-right of array)
        prev_row = [0]*n      #initialize a row of same length as the rows

        for row in range(m - 1, -1 ,-1):    #step through rows from bottom to top
            curr_row = [0]*n                #for each step, make a "current" row to fill using previous row
            curr_row[-1] = 1                #intialize rightmost element to 1, since that's guaranteed on right side
            for col in range(n - 2, -1 ,-1):    #now step through the remaining columns (don't include rightmost) to fill current row
                curr_row[col] = curr_row[col + 1] + prev_row[col]   #the element at this index is sum of element to its right, and below it

            prev_row = curr_row     #after filling current row, set this to the previous row, and move up to next row

        return prev_row[0]  #the solution is the element in top left of the matrix

# time: O(n*m)
# space: O(n)