class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = 0
        curr_max = 0 

        for val in nums:
            if val == 1:
                curr_max += 1
                max_consec = max(curr_max, max_consec)
            else:
                curr_max = 0
                
        return max_consec
            
