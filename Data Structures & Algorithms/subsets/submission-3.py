class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # dfs. backtracking
        if not nums:    
            return []
    
        res = []   #want to return a list of sublists
        
        def backtrack(path, i):
            res.append(list(path))  #append copy of the current path to result

            for j in range(i, len(nums)):
                path.append(nums[j])   #we use the current value
                backtrack(path, j + 1)

                path.pop() #and then remove the value after recursing


        backtrack(path=[], i = 0)   #start with empty list and index 0 
        return res

# time: O(n*2^n)
# space: O(n)