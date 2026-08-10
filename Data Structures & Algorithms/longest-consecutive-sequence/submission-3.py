class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        starts = set()  #set to store starting vals of possible sequences
        nums_set = set(nums)    #converting nums to a set
        for val in nums_set:  #go though all vals in nums and check if any have a neighboring val 
            if val - 1 not in nums_set: #if there is no previous neighboring val, then it's a possible start
                starts.add(val)

        longest = 0     #variable to store longest sequence
        for val in starts:  #loop through possible sequence starts
            curr_longest = 1    
            while val + 1 in nums_set:  #if there's a neigboring integer (+1), then continue the sequence
                curr_longest += 1
                val += 1
            longest = max(longest, curr_longest)    #and store the longest sequence lenght
    
        return longest

# time: O(n)
# space: O(n)