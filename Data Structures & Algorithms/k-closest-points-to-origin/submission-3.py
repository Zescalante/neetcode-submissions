class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def quickSort(arr, s, e):
            if e - s + 1 <= 1:  #if the arr is a single element, just return the array
                return arr
            
            pivot = arr[e]
            left = s

            for i in range(s, e):
                if arr[i][0]**2 + arr[i][1]**2 < pivot[0]**2 + pivot[1]**2:
                    temp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = temp
                    left += 1
                
            arr[e] = arr[left]
            arr[left] = pivot

            quickSort(arr, s, left - 1) #quicksort to left of pivot 
            quickSort(arr, left + 1, e) #quicksort to right of pivot 

            return arr


        if not points:
            return []


        res = quickSort(points, 0, len(points) - 1)

        return res[:k]