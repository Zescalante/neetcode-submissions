class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # find the integer with no duplicates.
        # one single variable to hold the key element.
        # Set solution
        seen = set()    #store elements from nums. Only non-duplicate should remain
        for val in nums:    #loop through arr
            if val in seen: seen.remove(val)    #if we've seen the el, then remove
            else: seen.add(val) #otherwise we add it
        return seen.pop()   #should only be one element left. pop and return

# time: O(n)
# space: O(1)