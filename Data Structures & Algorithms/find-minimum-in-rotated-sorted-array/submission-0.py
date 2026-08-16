class Solution:
    def findMin(self, nums: List[int]) -> int:
        # all unique elements. binary sort involved, since O(logn)?

        # find pivot with binary and then another binary    
        l, r = 0, len(nums) - 1

        while l < r:   #we don't want pointers to be the same
            mid = (l + r) // 2  
            if nums[mid] > nums[r]: #if nums[mid] gt nums[r], then right half has the smallest val
                l = mid + 1 #so move left pointer in
            else: #else left half contains the min value. Could be nums[mid] itself
                r = mid #move r to mid, NOT mid - 1, since nums[mid] could be the minimum
        return nums[l]  #at the end, l pointer will have the min element

# time: O(logn)
# space: O(1)