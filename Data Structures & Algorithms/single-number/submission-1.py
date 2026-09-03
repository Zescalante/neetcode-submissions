class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # OPTIMAL SOLUTION. Bitwise
        res = 0
        for val in nums:
            res ^= val
        
        return res

# time: O(n)
# space: O(1)