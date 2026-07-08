class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []        #final result array
        sub = []        #array to hold path of values currently being taken

        def dfs(i, curr_path, curr_target):     #backtracking with starting index, current path, and current target value
            if curr_target == 0:                #if we've hit the target value
                res.append(list(curr_path))     #then add the path to the final array
                return                          #and step out of the recursive call

            for i in range(i, len(nums)):       #otherwise we haven't hit the target
                if nums[i] <= curr_target:      #so check if we can still add values
                    curr_path.append(nums[i])   #if yes, add the value nums[i]
                    dfs(i, curr_path, curr_target - nums[i])    #and recurse with new current target, staying at index i in case we can use it again

                    curr_path.pop()             #remove the value from the current path so we can explore other values

            

        dfs(0, sub, target)     #pass in start of 0, empty path arr, and original target value
        return res              #return the final array