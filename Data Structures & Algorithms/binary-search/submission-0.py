class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #Classic binary search

        l, r = 0, len(nums) - 1 #set the left and right index pointers at the start and end of the array
        
        while l <= r:           #while the left pointer is to the left of the right pointer
            mid = (l + r)//2    #calculate the middle index. Rounded down to nearest integer

            if target < nums[mid]:     #if the target value is less than the value at mid index
                r = mid - 1            #then move the right pointer in, just to the left of the mid index
            elif target > nums[mid]:   #if target value is greater than the value at mid index
                l = mid + 1            #then move left pointer in, just to the right of the mid index
            else:                      #else the target value equals the value at mid index
                return mid           #so return the index, as requested

        return -1           #otherwise, value doesn't exist in the array, so return -1

# time: O(logn)
# space: O(1)