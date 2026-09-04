class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # optimal solution. bitwise XOR
        seen = set(nums)
        size = len(nums) #max value seen in the list
        res = 0
        for val in range(size + 1):
            res ^= val
        
        for val in seen:
            res ^= val
        return res
            
# time: O(n)
# space: O(n)