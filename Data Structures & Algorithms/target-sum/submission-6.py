# TOP DOWN DP MEMOIZATION
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        print(nums)

        seen = {}

        def backtrack(i, tot_sum):

            if i == len(nums):
                if tot_sum == target:
                    return 1    #one contributino 
                else:
                    return 0 

            if (i, tot_sum) in seen:
                return seen[(i, tot_sum)]

            seen[(i, tot_sum)] = backtrack(i + 1, tot_sum - nums[i]) + backtrack(i + 1, tot_sum + nums[i])

            return seen[(i, tot_sum)]

        return backtrack(0, 0)
        

        