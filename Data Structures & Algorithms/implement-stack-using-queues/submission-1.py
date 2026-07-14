from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()   #the "true" stack
        self.q2 = deque()   #the temp storage queue
        

    def push(self, x: int) -> None:
        self.q2.append(x)   #add the new element to the temp queue

        
        while self.q1:      #popleft from q1 and add to q2. 
            self.q2.append(self.q1.popleft())

        #now the "top" of the stack is the front

        self.q1, self.q2 = self.q2, self.q1 #rename the stacks

    def pop(self) -> int:

        return self.q1.popleft()  #the "top" of the stack is the front. So just popleft()
        

    def top(self) -> int:

        return self.q1[0]   #we're allowed to "peek" at top of stack
        

    def empty(self) -> bool:
        
        return not self.q1  #if q1 is empty, return True. Else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()