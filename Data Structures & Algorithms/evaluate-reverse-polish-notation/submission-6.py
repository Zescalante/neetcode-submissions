class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  #stack for LIFO for operations

        for c in tokens:    #single pass through the tokens
            if c not in ['-','+','*','/']:  #if the token is a number
                stack.append(int(c))    #then just add to the stack as an int

            else:   #otherwise it's an operation    
                y, x = stack.pop(), stack.pop() #so pop last two elements
                if c == '-':    #and perform the operation
                    stack.append(x - y)
                elif c == '+':
                    stack.append(x + y)
                elif c == '*':
                    stack.append(x * y)
                else:   #for div, we want truncation towards 0, so use int()
                    stack.append(int(x / y))

        return stack[0] #should only be one element left in stack. That's the answer

# time: O(n); n = length of array
# space: O(n)