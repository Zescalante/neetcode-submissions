class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # integer n means n pairs, so 2n characters. backtracking?
        # count of closing brackets can't exceed count of open
        res = [] #store subarrays in final arr
        
        def backtrack(substr, opening, closing):

            if len(substr) == 2*n:  #if we've hit the character limit
                res.append(substr)  # add to result and exit call
                return

            if opening < n:    #as long we haven't placed > n opening (, then we can add one
                backtrack(substr + "(", opening + 1, closing)
            if closing < opening:   #and as long as we haven't placed too many ), add one
                backtrack(substr + ")", opening, closing + 1)
        
        backtrack("", 0, 0) #call backtrack with empty string and 0 initial parentheses
        return res

# time: O(4^n / sqrt(n))
# space: O(n)