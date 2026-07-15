#TOP-DOWN MEMOIZATION SOLUTION

class Solution:
    def rob(self, nums: List[int]) -> int:

        def memoization(i, cache):  #take parameters of house at index i, and a cache for history 
            if i >= len(nums):      #if we've hit the end of houses, or gone past
                return 0            #then return 0 since there's no money here

            if i in cache:          #check if we've already checked this house
                return cache[i]     

            # add the maximum of skipping this house and robbing the adjacent one, or robbing this one and skipping over a house
            cache[i] = max(nums[i] + memoization(i + 2, cache), memoization(i + 1, cache))

            # return the amount of money
            return cache[i]

        #call memoization starting at house 0, with an empty cache
        return memoization(0, {})

# time: O(n)
# space: O(n)