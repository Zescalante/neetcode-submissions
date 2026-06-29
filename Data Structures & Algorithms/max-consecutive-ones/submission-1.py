class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_len = 0 #variable to hold max consecutive ones
        count = 0 #temp counter in loop

        for i in range(len(nums)): #loop through list
            if nums[i] == 1:       #if the value at index i is 1
                count += 1         #increase temp counter by 1

            else:                  #else if the value at i is 0
                count = 0          #reset the temp counter

            max_len = max(max_len, count)   #store the maximum of the temp counter and max length variable

        return max_len   #return max_len

        # Time: O(n)
        # Space: O(1)
            