class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig_color = image[sr][sc]  #first store the original color at the input indices

        if orig_color == color:     #if the original color and the desired color already match
            return image            #then we don't need to recurse; just return the image

        def dfs(arr, start_r, start_c, val):    #dfs helper. In put the arr, start r and c, and desired color
            rows, cols = len(arr), len(arr[0])  #get the size of the array
            
            #if we're out of bounds...
            if (min(start_r, start_c) < 0) or \
            (start_r == rows) or \
            (start_c == cols) or \
            (arr[start_r][start_c] != orig_color):  #or the current pixel is not original color
                return                           #exit the recursive loop   

            arr[start_r][start_c] = val         #otherwise, set the pixel value to the desired color

            dfs(arr, start_r + 1, start_c, val) #then step down,
            dfs(arr, start_r - 1, start_c, val) #up,
            dfs(arr, start_r, start_c + 1, val) #right,
            dfs(arr, start_r, start_c - 1, val) #and left, recursively 

            return arr          #after all recursive calls are done, return the modified arr

        return dfs(image, sr, sc, color)        #call dfs with the input parameters!

    
    # time: O(4^(nm))
    # space: O(nm)