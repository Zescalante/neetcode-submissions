class ListNode:
    #usual doubly linked list node class
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next 

class BrowserHistory:

    def __init__(self, homepage: str):
        head = ListNode(homepage)      #make the homepage node. Currently no forward or backward nodes

        self.curr = head               #set the current page to the homepage

    def visit(self, url: str) -> None:
        new_node = ListNode(url)       #make a new node for the new page to visit

        new_node.prev = self.curr      #connect the new node before disconnected the old current node. Set new node prev to curr
        self.curr.next = new_node      #now point curr.next to the new node
        self.curr = new_node           #and move the current node pointer to the new node
                                       #since new_node.next set to None by default, we lose forward history, as we wanted


    def back(self, steps: int) -> str:
        
        for _ in range(steps):      #make a loop to move #steps through the history
            if self.curr.prev:      #if there's a previous page to move back to
                self.curr = self.curr.prev      #then step backwards once
            else:                   #otherwise if no previous page then no point in looping, so break out
                break    
        return self.curr.val        #return the value at the current node
        

    def forward(self, steps: int) -> str:

        for _ in range(steps):      #same as in previous, but moving forward
            if self.curr.next:
                self.curr = self.curr.next
            else: 
                break
    
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)