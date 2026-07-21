#RECURSIVE SOLUTION WITH MEMOIZATION
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        visited = {}

        # implementing dfs 
        def dfs(idx, tot_sum):

            if idx == len(nums):    #base case. If we've hit the end of the array
                if tot_sum == target:   #then check if we've hit the target exactly
                    return 1            #if so, this is one possible way
                else:                   #otherwise we didn't hit the target 
                    return 0            #so no contribution

            if (idx, tot_sum) in visited:  
                return visited[(idx, tot_sum)]
            
            #we want to return the number of ways, so we sum paths taken either 
            #subtracting or adding the current value to the running sum
            visited[(idx, tot_sum)] = dfs(idx + 1, tot_sum - nums[idx]) +  dfs(idx + 1, tot_sum + nums[idx]) 

            return visited[(idx, tot_sum)]

        return dfs(0, 0)   #we call dfs with 0 starting index and an initial sum of 0

# time: O(2^n)
# space: O(n)