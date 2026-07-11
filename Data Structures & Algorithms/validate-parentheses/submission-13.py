class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2 or not s:
            return False

        lookup = {')':'(',']':'[','}':'{'}
        stack = []

        for char in s:
            if char in lookup.keys():   #if we have a closing bracket   
                if (not stack) or (lookup[char] != stack[-1]):  #check if list is empty or the most recent in stack doesn't close the bracket
                    return False
                stack.pop()     #if yes, we can remove from the stack


            else:   #otherwise it's an opening bracket
                stack.append(char)  #so just add to the stack
        
        return not stack