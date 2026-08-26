class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking dfs
        res = [] #store the answer 

        candidates.sort() #time: O(nlogn)
        def dfs(i, curr_sum, subarr):

            # if i == len(candidates):
            if curr_sum == target:
                res.append(list(subarr))
                return 

            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue

                elif curr_sum + candidates[idx] <= target:
                    subarr.append(candidates[idx])
                    dfs(idx + 1, curr_sum + candidates[idx], subarr)
                    subarr.pop()

        dfs(i=0, curr_sum=0, subarr=[])

        return res


# time: O(n*2^n)
# space: O(n)