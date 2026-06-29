class Solution:
    def isValid(self, s: str) -> bool:
        brack_dict = {"(": ")", "[": "]", "{": "}"} #dict to match corresponding brackets
        stack = []  #array to hold unclosed brackets

        for i,c in enumerate(s):    #loop through the input list

            if c in brack_dict.keys(): #if c is an opening bracket
                stack.append(c) #put it in the stack
            # elif brack_dict[stack[-1]] == c: #or if c is a matching closing bracket
            #     stack.pop()     #pop from the stack
            elif c in brack_dict.values():
                if not stack:
                    return False
                elif brack_dict[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
                
            # else:               #else, if c is a non-matching closing bracket
            #     return False    #it's an invalid string, and return False

        return not stack        #if the stack is empty, return True, else return False