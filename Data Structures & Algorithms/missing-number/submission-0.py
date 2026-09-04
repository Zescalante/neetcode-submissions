class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums) #max value seen in the list

        for val in range(size + 1):
            if val not in nums:
                return val
            
# time: O(n)
# space: O(1)