class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # backtracking?
        res = [] #store subarrs in arr

        def backtrack(path, start):#track curr substring (path list) and curr index
            if start == len(s):   #if our start index reaches the end
                res.append(list(path))  #then we copy current path to result arr

            for end in range(start + 1, len(s) + 1):    #else we iterate over remaining indices
                sub = s[start:end]  #get the substring

                if sub[:] == sub[::-1]: #and if it's a palindrome
                    path.append(sub)    # add the char to the curr path list
                    backtrack(path, end)    #recurse with new path and end  
                    path.pop()  #and then remove the char
            
        backtrack([], 0)    #call with empty path and index 0 to start

        return res
        
# time: O(n * 2^n)
# space: O(n)