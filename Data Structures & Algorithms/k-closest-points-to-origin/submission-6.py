class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #quick sort solution

        if not points:
            return []

        size = len(points)

        def quicksort(arr, s, e):
            if e - s + 1 <= 1:
                return arr
            
            pivot = arr[e]
            left = s

            for i in range(s, e):
                # if arr[s] < pivot:
                if arr[i][0]**2 + arr[i][1]**2 < pivot[0]**2 + pivot[1]**2:
                    temp = arr[left]
                    arr[left] = arr[i]
                    arr[i] = temp
                    left += 1

            arr[e] = arr[left]
            arr[left] = pivot

            quicksort(arr, s, left - 1)
            quicksort(arr, left + 1, e)

            return arr

        quicksort(points, 0, size - 1)

        return points[:k]



    