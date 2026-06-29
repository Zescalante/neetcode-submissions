class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_el = -1
        # curr_el = 0
        for i in range(len(arr)-1, -1, -1):
            curr_el = arr[i]
            arr[i] = max_el
            max_el = max(max_el, curr_el)
            # print(arr)

        return arr

