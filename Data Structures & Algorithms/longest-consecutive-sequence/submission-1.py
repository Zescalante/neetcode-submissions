class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        starts = set()
        nums_set = set(nums)
        for i, val in enumerate(nums):
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