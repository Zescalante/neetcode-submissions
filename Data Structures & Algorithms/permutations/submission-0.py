class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking? Input has unique integers. No replacement

        seen = set() #store seen indices

        def dfs(sublist):

            if len(sublist) == len(nums):   #if we maxed out length of sublist
                res.append(list(sublist))   #then make a copy and append to result

            for j in range(len(nums)):      #iterate through all indices 
                if j not in seen:        #if the index hasn't been visited
                    seen.add(j)          #then add to visits
                    sublist.append(nums[j]) #and add the element to the sublist
                    dfs(sublist)        #and recurse with the updated sublist
                    seen.remove(j)      #afterwards, remove the index from visits
                    sublist.pop()       #and pop the latest element from sublist

        res = []    #list to hold the sublists
        dfs([])     #run dfs with an empty sublist
        
        return res

# time: O(n*n!)
# space: O(n)