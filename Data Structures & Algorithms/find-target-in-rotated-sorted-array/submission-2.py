class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(logn) time means binary search?
        
        #binary search to find pivot index
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            #first just check if we found the target
            if nums[mid] == target:
                return mid

            # one side of the array MUST be sorted
            #checking the left sorted portion
            if nums[left] <= nums[mid]:
                # if left side is sorted, then check if target is in there
                if nums[left] <= target < nums[mid]:
                    #if yes, then we move right index in
                    right = mid - 1
                    #otherwise it's not, so move the left in
                else:
                    left = mid + 1
            # or check the right portion
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1   #if the target is not in the array, then return -1

# time: O(logn)
# space: O(1)
        
