#TOP-DOWN DP
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2) #get size of strings
        
        def dfs(i, j, cache):

            if i >= len1 or j >= len2:      #if we've gone out of bounds
                return 0                    #just return 0. No addition to results
            if (i, j) in cache:         #check if this location has been visited
                return cache[(i,j)]     #if so, just return that value

            if text1[i] == text2[j]:    #if the characters match
                cache[(i,j)] = 1 + dfs(i + 1, j + 1, cache) #we increment LCS by 1 and recurse stepping diagonally 
            else:       #otherwise the characters don't match
                cache[(i,j)] = max(dfs(i + 1, j, cache), dfs(i, j + 1, cache))  #so search by incrementing text1 or text2, and storing the max

            return cache[(i,j)]     #return the LCS at this location

        return dfs(0, 0, {}) #start at beginning of strings, and empty hashmap

    # time: O(n*m)
    # space: O(n*m)