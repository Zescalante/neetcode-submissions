class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # hashset solution 
        seen = set(nums)
        size = len(nums) #max value seen in the list

        for val in range(size + 1):
            if val not in seen:
                return val
            
# time: O(n)
# space: O(n)