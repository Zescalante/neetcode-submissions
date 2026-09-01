class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # mapping -> hashmap? digits can be [2,9]. Max length 4.
        res = []    #store the result in an array
        mapping = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g","h","i"],\
        "5": ["j","k","l"], "6": ["m","n","o"], "7": ["p","q","r","s"],\
        "8": ["t","u","v"], "9": ["w","x","y","z"]}

        if not digits: return []    #base case if there's no digits
        
        def dfs(idx, substr):   #dfs tracking index of digits arr and current substring "path"
            if idx == len(digits):  #if we're at the end of digits, then add to result and exit call
                res.append(substr)
                return

            letters = mapping[digits[idx]] #get the array of letters for this digit
            for l in letters:   #loop through those letters
                dfs(idx + 1, substr + l)    #move on to next index with new substring path

        dfs(0, "")
        return res

# time: O(n*4^n)
# space: O(n)