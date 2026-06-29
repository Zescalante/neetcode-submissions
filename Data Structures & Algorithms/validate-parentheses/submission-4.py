class Solution:
    def isValid(self, s: str) -> bool:
        diction = {"(": ")", "[": "]", "{": "}"} #Dictionary to relate brackets
        arr = []                                 #Initialize stack
        for i, char in enumerate(s):             #loop through input array
            if char in ["(","[","{"]:            #if it's an opening bracket
                arr.append(char)                 #append the char to the stack
            elif char in [")","]","}"]:          #if it's a closing bracket
                if len(arr) == 0:                #then if the stack is empty 
                    return False                 #return False
                elif char == diction[arr[-1]]:   #or if the brackets match up
                    arr.pop()                    #then pop the last element from the stack
                else:                            #otherwise
                    return False                 #Return False

        return True if len(arr) == 0 else False  #if there's nothing left in the stack then it's valid, otherwise not valid

