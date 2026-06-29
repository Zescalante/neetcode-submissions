class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We're merging two sorted arrays. Need pointers i,j for each array

        i = m - 1       #index of last valid element in nums1
        j = n - 1       #index of last el in nums2
        k = m + n - 1   #index of last el in nums1

        # moving from the end of nums1 array, since that's where the empty space is
        while j >= 0:           #while we have values in nums2 to check
            if i >= 0 and nums1[i] > nums2[j]:  #if we're not at the start of nums1, and if num1[i] has the larger el
                nums1[k] = nums1[i]             #then set nums1 at k index (the very end) to the greater value
                i -= 1                          #now decrement i to look at the next left el in nums1
            else:                               #otherwise
                nums1[k] = nums2[j]             #nums2 at index j has the larger value, so put that in num1[k]
                j -= 1                          #and decrement j
            k -= 1                              #place k of nums1 has been filled, so decrement and move to next position

        # while j > 0:                       #if there's still els in nums2 to look at 
        #     nums1[k] = nums2[j]            #place them in the remaining spots for nums1
        #     j -= 1
        #     k -= 1

# time: O(m + n)
# space: O(1)

