class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1   #set the curr_max to -1, since we want that at the end of arr

        for i in range(len(arr) - 1, -1, -1):   #step backwards through arr
            temp = arr[i]               #first store the val at the current index
            arr[i] = curr_max           #then place the current max at i
            curr_max = max(temp, curr_max)  #then find the new current max between temp and old current max
    
        return arr      #return the rearranged arr