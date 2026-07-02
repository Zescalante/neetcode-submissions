class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #stepping through array backwards 
        curr_max = -1   #starting with -1 since we want -1 as the last element anyway

        for i in range(len(arr) - 1, -1, -1):
            curr_el = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_el, curr_max)
             
        return arr
