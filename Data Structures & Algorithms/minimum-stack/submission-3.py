class MinStack:

    def __init__(self):
        self.stack = [] #Initialize the empty stack by default. No input arguments
        self.min_stack = [] #Initialize empty stack to hold the min val at the time

    def push(self, val: int) -> None:
    
        if not self.min_stack:                  #if the min stack is empty
            self.min_stack.append(val)          #then we push the current val as the min val
        else:                                   #otherwise
            self.min_stack.append(min(val, self.min_stack[-1]))     #append the min of either the input val or the last element to the min stack
        self.stack.append(val)                                      #and append the val to the regular stack

    def pop(self) -> None:                                   
        self.stack.pop()                            #remove the last element from stack
        self.min_stack.pop()                        #remove the last element from the min stack 


    def top(self) -> int:
        return self.stack[-1]                       #return the last val of the stack. Don't remove (pop) it
        
    def getMin(self) -> int:
        return self.min_stack[-1]                   #return the current minimum value of the stack
        
# time: O(1)
# space: O(n)
