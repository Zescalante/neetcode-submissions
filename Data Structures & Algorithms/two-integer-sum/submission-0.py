class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diction = {}        #dictionary to store value, index pairs
        for i in range(len(nums)):  #loop through value in nums
            diff = target - nums[i] #calculate the difference between target and nums[i]

            if diff in diction:             #if we've seen this difference before
                return [diction[diff], i]   #then we've found our index pair; return the indices
            else:                           #else we haven't seen this difference before
                diction[nums[i]] = i        #so add the difference and index to the dictionary
            #we're guaranteed to find a pair, so no need for final checks
# time: O(n)
# space: O(n)