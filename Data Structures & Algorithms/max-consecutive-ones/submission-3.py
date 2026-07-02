class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0     #holds the max consecutive ones
        curr_count = 0    #holds the current count of ones

        for val in nums:  #loop through each of the vals in the array
            if val == 1:  #if the value is one
                curr_count += 1 #increment the current count
            else:               #otherwise the value is zero
                curr_count = 0  #so reset the current counter
            max_count = max(curr_count, max_count)  #compare curr and old max count. Take the maximum
        
        return max_count    #return the maxiumum consecutive ones

# time: O(n) 
# space: O(1)
                 