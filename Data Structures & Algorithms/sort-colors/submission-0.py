class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Perfect case for a bucket sort

        counts = [0]*3 #initialize an array. Length is number of unique vals   

        for val in nums:       #loop through the numbers in the list 
            counts[val] += 1   #increment the count. Convenient since the numbers correspond to their indices
        
        i = 0      #index to replace the next value in the original array

        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[i] = n
                i += 1

# time: O(n) the beauty of bucket sort
# space: O(1) 
