class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # BUCKET SORT
        counts = [0]*3      #we know how many unique values there are: 3. Initialize an array this size

        for val in nums:        #for each value we see in nums
            counts[val] += 1    #increment the counter array for that value. The index is the value in this case

        i = 0                    #final placement index in nums array. This will always be incremented
        for val in range(len(counts)):      #for each value in counts (the index is the value in this case)
            for _ in range(counts[val]):    #"dummy" loop to keep incrementing i
                nums[i] = val               #filling the original array with the value _ times
                i += 1                      #and incrementing 
        
        return nums