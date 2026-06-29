class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We're merging two sorted arrays. Need pointers i,j for each array

        # k = m + n 
        # i , j = 0
        

        # while i < size and j < n:

        #     if nums1[i] <= nums2[j]:
        #         nums1[k] = nums1[i]
        #         i += 1
        #     else:
        #         nums1[k] = nums2[i]
        #         j += 1

        i = m - 1       #index of last valid element in nums1
        j = n - 1       #index of last el in nums2
        k = m + n - 1   #index of last el in nums1

        # for k in range(m + n - 1, -1, -1):
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


        # while i >= 0 and j >= 0:

            # if nums1[i] >= nums2[j]:
            #     nums1[k] = nums1[i]
            #     i -= 1
            # else:
            #     nums1[k] = nums2[j]
            #     j -= 1
            
            # k -= 1

        



