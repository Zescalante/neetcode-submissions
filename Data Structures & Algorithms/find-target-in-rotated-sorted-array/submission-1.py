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
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[right] > nums[mid]:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
