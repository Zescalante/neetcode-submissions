class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #dfs with backtracking
        res = []
        def dfs(curr_sum, sublist, i):
            
            if curr_sum == 0: 
                res.append(list(sublist))
                return  

            for idx in range(i, len(nums)):
                if nums[idx] <= curr_sum:
                    sublist.append(nums[idx])
                    dfs(curr_sum - nums[idx], sublist, idx)

                    sublist.pop()
                    

        dfs(target, [], 0)

        return res