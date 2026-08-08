class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        hashmap = {'(': ')', '[': ']', '{': '}'}
            
        if len(s) == 1:
            return False

        stack = []
        for c in s:  
            #if it's an opening bracket
            if c in hashmap.keys():
                stack.append(c)
                continue

            # if it's a closing bracket
            if c in hashmap.values():
                if not stack:
                    return False

                elif hashmap[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return not stack
    
    






# time: O(n) 
# space: O(n) 