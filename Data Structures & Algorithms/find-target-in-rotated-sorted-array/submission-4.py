class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # since we want O(logn), must be binary search. we know one of the halfs must be the sorted half, since it's in ascending order

        left, right = 0, len(nums) - 1 #initialize l, r pointers for binary search

        while left <= right: # first we find the "pivot" index, which is in the non-sorted half
            mid = (left + right) // 2   #find the middle index

            if nums[mid] == target: #check if we happened to find the target index
                return mid

            if nums[left] <= nums[mid]: #if left val less than (or equal) to mid val, then left half is sorted
                if nums[left] <= target < nums[mid]:    #so check if the left half can contain the target val
                    right = mid - 1 #if so, move in right pointer, since target must be in left half   
                else: 
                    left = mid + 1 #otherwise it's in the right half

            else:   #vice versa. Here we check the right half
                if nums[mid] < target <= nums[right]: 
                    left = mid + 1
                else: 
                    right = mid - 1

        return mid if nums[mid] == target else -1

# time: O(logn)
# space: O(1)