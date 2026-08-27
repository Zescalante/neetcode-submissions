class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking dfs?
        res = []    #store the result in arr
        seen = set()    #a set to track seen values
        def dfs(sub, seen):
            if len(sub) == len(nums):   #if we hit the length limit
                res.append(list(sub))   #then add copy of sublist to result 
                return  #and exit the recursive cal
            
            for idx in range(len(nums)):  #step through all values
                if nums[idx] in seen:   #if the val has been seen
                    continue    #then skip
                seen.add(nums[idx]) #otherwise we add val to seen set
                sub.append(nums[idx])   #and to the subarray    
                dfs(sub, seen)  #recurse 
                seen.remove(nums[idx])  #and then remove from both
                sub.pop()
                
        dfs([], seen)
        return res

# time: O(n*n!)
# space: O(n)