class Solution:

    #implementing the quicksort algo verbatum from the lesson, with some minor tweaks
    def quickSort(self, arr: List[List[int]], s: int, e: int) -> List[List[int]]:
        # s and e are the start and end indices that quicksort will look between

        if e - s + 1 <= 1:  #if we're only looking at a list of one value, then return the array
            return arr

        pivot = arr[e]      #choosing the rightmost value (array in this case) as the pivot
        left = s            #set left to the start index

        # this is the partition. Elements smaller than pivot go to the left 
        for i in range(s, e):       #step through start to end indices

            # this next line is the big difference. We compart euclidean magnitudes of the points, instead of plain values
            # if the magnitude of point arr[i] is less than pivot point mag
            if (arr[i][0]**2 + arr[i][1]**2) < (pivot[0]**2 + pivot[1]**2):

                temp = arr[left]        #store the current points at left index
                arr[left] = arr[i]      #point at index i now goes to index left
                arr[i] = temp           #and point at i is now the old point at left
                left += 1               #and step left forward because we don't want to overrwrite

        arr[e] = arr[left] #now move the pivot to where the left index ended up, and vice versa
        arr[left] = pivot

        self.quickSort(arr, s, left - 1)    #now run the same process on the points left of the pivot

        self.quickSort(arr, left + 1, e)    #and to the right of the pivot. No need to include pivot itself

        return arr          #and return the sorted list of points

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        if points:      #Checking that there are points in the list to begin with

            res = self.quickSort(points, s=0, e=(len(points) - 1)) #run quickSort from start to end of the list!


        return res[:k]      #and return the first k sorted points!
    
# time: O(nlogn)
# space: O(n)
