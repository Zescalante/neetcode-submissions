class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking dfs.
        res = [] #store the answer 

        candidates.sort() #sort values for simple duplicate skipping. time: O(nlogn)
        def dfs(i, curr_sum, subarr):   #we're tracking the list index, current sum, and subarr

            if curr_sum == target:  #base: check if our sum has met target value
                res.append(list(subarr))    #if yes, append copy of subarray to result
                return  #and exit current call

            for idx in range(i, len(candidates)):   #step through remaining indices
                if idx > i and candidates[idx] == candidates[idx - 1]:  
                    continue #check if subsequent elements are duplicate of previous. if yes, skip

                elif curr_sum + candidates[idx] <= target:  #else if we can still add towards target
                    subarr.append(candidates[idx])  #then add el to subarr
                    dfs(idx + 1, curr_sum + candidates[idx], subarr)    #call dfs
                    subarr.pop()    #and pop the element afterwards

        dfs(i=0, curr_sum=0, subarr=[])

        return res


# time: O(n*2^n)
# space: O(n)