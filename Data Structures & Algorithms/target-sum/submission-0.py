class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # print(nums)
        #recursion. DFS?

        # total_sum = 0 
        # count = 0 #number of ways to reach the target
        
        def dfs(idx, tot_sum):
            # run_sum = 0

            if idx == len(nums):
                if tot_sum == target:
                    return 1
                else:
                    return 0

            # tot_sum += dfs(idx + 1, tot_sum - nums[idx]) 
            # tot_sum += dfs(idx + 1, tot_sum + nums[idx])

            # return tot_sum

            return dfs(idx + 1, tot_sum - nums[idx]) +  dfs(idx + 1, tot_sum + nums[idx]) 

        return dfs(0, 0)