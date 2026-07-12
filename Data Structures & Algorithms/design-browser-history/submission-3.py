class ListNode:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        home = ListNode(homepage)   #make the homepage node
        
        self.curr = home        #and set it as the current node

    def visit(self, url: str) -> None:
        new_page = ListNode(url)    #make the new page
        self.curr.next = new_page   #point the current node's next to the new url
                                    #forward history cleared automatically
        new_page.prev = self.curr   #and connect the new page back to current page

        self.curr = new_page        #set the new current page
        

    def back(self, steps: int) -> str:

        for _ in range(steps):      #for the desired number of steps
            if self.curr.prev:      #if there's a prev node
                self.curr = self.curr.prev  #then step into it
            else:                   #otherwise, no previous node; we've hit the homepage
                break               #so break out
        
        return self.curr.val        #return the url

    def forward(self, steps: int) -> str:
        
        for _ in range(steps):      #same as back, but going forward
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