class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) #store the length of the array
        current_max = -1 #Current max val. Start with -1 since we need that at the end of the array
        for i in range(n-1,-1,-1): #Step backwards through the array 
            current_val = arr[i]   #Store the array value at index i
            arr[i] = current_max   #Update the value at index i to the current max (-1 to start)
            current_max = max(current_val, current_max) #Now update the current max value between the original value at i, and the current max

        return arr

#time: O(n)
#space: O(1)
