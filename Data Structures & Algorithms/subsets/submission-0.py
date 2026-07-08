class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:        #edge case if the initial array is empty
            return []

        res = [] #array to hold final list

        def dfs(path, start): #depth-first with backtracking. Not with nodes, but arrays
            res.append(list(path))

            for i in range(start, len(nums)): #only loop from starting index to end

                path.append(nums[i])

                dfs(path, i + 1)

                path.pop()


        dfs(path = [], start = 0)

        return res
