class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] #empty array to hold the subarray
        sub = [] #empty array to hold subarray values

        def dfs(idx):       #backtracking dfs with only index as parameter
            if idx >= len(nums): #if I has reached the length (end) of the original arr
                res.append(list(sub)) #subarr is complete, so append to result arr
                return                #and step out of call
            
            #if we're including the value in the subarray
            sub.append(nums[idx])     #otherwise we add nums[i] to the subarray
            dfs(idx + 1) #and recurse to next index in array

            #if we're not including the value in the subarray
            sub.pop()           #remove the value from the subarray
            dfs(idx + 1)        #recursive call again to next branch 
        
        dfs(0)  #call the function starting from the beginning index
        return res      #return the final array

# time: O(n*2^n)
# space: O(n*2^n)
