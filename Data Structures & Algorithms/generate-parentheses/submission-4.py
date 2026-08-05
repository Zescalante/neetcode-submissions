class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #n = pairs of parentheses
        res = []
        #we track current string being built, and the number of open and closed parentheses currently used
        def backtrack(string, open, close):
            if open == close == n:  #base. If we've hit the length limit
                res.append(string)  #then we append the string

            if open < n:    #otherwise, if open parenthesis count is less than half tot length limit
                backtrack(string + "(", open + 1, close)    #then we recurse with another ( and count open + 1 

            if close < open:    #then, if count of close ) is less than that of open (, 
                backtrack(string + ")", open, close + 1)    #then recurse with that

        backtrack("", 0, 0) #call dfs with empty string, and 0 current parentheses

        return res
# time: O(4^n / sqrt(n)); n = pairs of parentheses
# space: O(n)