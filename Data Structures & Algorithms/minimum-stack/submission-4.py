class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)  #append (push) the val to the stack
        
        if not self.minstack:   #if the minstack stack is empty
            self.minstack.append(val)   #just append the val to minstack 
        else:                       #otherwise
            self.minstack.append(min(val, self.minstack[-1]))   #append the minimum of the last val in minstack, or the given value

    def pop(self) -> None:
        self.stack.pop()        #pop (remove) the last val of the stack. LIFO!
        self.minstack.pop()     #and pop the last val of the minstack, to track the new minimum value
        

    def top(self) -> int:   

        return self.stack[-1]   #just return the last element of the stack
        

    def getMin(self) -> int:
        
        return self.minstack[-1] #return the last element of the min value stack
        
