class Solution:
    def isValid(self, s: str) -> bool:
        brack_dict = {"(": ")", "[": "]", "{": "}"} #dict to match corresponding brackets
        stack = []  #array to hold unclosed brackets

        for i,c in enumerate(s):    #loop through the input list

            if c in brack_dict.keys(): #if c is an opening bracket
                stack.append(c) #put it in the stack
            elif c in brack_dict.values(): #or, if c is a closing bracket
                if (not stack) or (brack_dict[stack[-1]] != c): #if the stack is empty or the brackets don't match up
                    return False
                stack.pop()

        return not stack        #if the stack is empty, return True, else return False