class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        starts = set()  #set to store starting vals of possible sequences
        nums_set = set(nums)    #converting nums to a set
        for val in nums_set:  
            if val - 1 not in nums_set:
                starts.add(val)

        longest = 0 
        for val in starts:
            curr_longest = 1 
            while val + 1 in nums_set:
                curr_longest += 1
                val += 1
            longest = max(longest, curr_longest)
    
        return longest

# time: O(n)
# space: O(n)