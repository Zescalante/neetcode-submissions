class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3

        for val in nums:
            counts[val] += 1

        i = 0       #placement index in nums array
        for val in range(3):
            for _ in range(counts[val]):
                nums[i] = val
                i += 1  
        
        return nums