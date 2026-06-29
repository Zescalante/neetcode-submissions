class ListNode: #A doubly-linked ListNode class

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = ListNode(homepage) #node for the homepage

        # self.head = ListNode(0) #sentinal head node
        # self.tail = ListNode(0) #sentinal tail node

        # self.homepage.next = self.tail #connect homepage node to sentinals. Point homepage next to sentinal tail
        # self.homepage.prev = self.head #Point homepage prev to sentinal head

        # self.curr = self.homepage

        self.current_node = self.homepage

        # self.head.next = self.homepage #Point the sentinals back to the homepage
        # self.tail.prev = self.homepage

        self.hist_len = 0  #initialize counter to track history length

        

    def visit(self, url: str) -> None:
        new_node = ListNode(url) #make the new node representing the new url

        curr = self.current_node #set the current node


        new_node.prev = curr
        curr.next = new_node
        new_node.next = None

        self.current_node = new_node



        # dummy_next = self.tail
        # dummy_prev = self.tail.prev
        

        # new_node.next = dummy_next.prev
        # new_node.prev = dummy_prev.next

        # dummy_next.prev = new_node.next
        # dummy_prev.next = new_node.prev


        

    def back(self, steps: int) -> str:

        curr = self.current_node
        for _ in range(steps):
            if curr.prev:
                curr = curr.prev
            else:
                break
        self.current_node = curr

        return self.current_node.val
        

    def forward(self, steps: int) -> str:

        curr = self.current_node
        for _ in range(steps):
            if curr.next:
                curr = curr.next
            else:
                break
        self.current_node = curr

        return self.current_node.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)