class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # since we want O(logn), must be binary search. we know one of the halfs must be the sorted half, since it's in ascending order

        left, right = 0, len(nums) - 1 

        # first we find the "pivot" index, which is in the non-sorted half
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: #check if we happened to find the target index
                return mid

            if nums[left] <= nums[mid]: #if left val less than mid val, then left half is sorted, so right half must have pivot
                if nums[left] <= target < nums[mid]: 
                    right = mid - 1 #move in right pointer, since target must be in left half
                else: 
                    left = mid + 1 #otherwise it's in the right half

            else:
                if nums[mid] < target <= nums[right]: 
                    left = mid + 1 #move in right pointer, since target must be in left half
                else: 
                    right = mid - 1 #otherwise it's in the right half

        return mid if nums[mid] == target else -1

# time: O(logn)
# space: O(1)