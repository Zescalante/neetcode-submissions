class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        
        hashmap = {}

        def dfs(i, j, cache):

            if i >= len1 or j >= len2:
                return 0
            elif (i, j) in cache:
                return cache[(i,j)]
            elif text1[i] == text2[j]:
                #extend subsequence
                cache[(i,j)] = 1 + dfs(i + 1, j + 1, cache)
            # elif text1[i] != text2[j]:
            else:
                cache[(i,j)] = max(dfs(i + 1, j, cache), dfs(i, j + 1, cache))

            return cache[(i,j)]


        



        return dfs(0, 0, hashmap)