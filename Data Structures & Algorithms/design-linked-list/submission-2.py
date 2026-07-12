class ListNode:

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):

        self.head = ListNode()
        self.tail = ListNode() #sentinal nodes for edge cases

        self.head.next = self.tail #connect the sentinals
        self.tail.prev = self.head #their other pointers are None by default

        self.size = 0   #initialize size to 0. Sentinals don't count 

    def get(self, index: int) -> int:
        
        if index >= self.size or index < 0:
            return -1

        else:
            curr = self.head.next 

            for _ in range(index):
                curr = curr.next

            return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)    #create the new node

        next_node = self.head.next  #store the original next node

        new_node.next = self.head.next   #attach the new node 
        new_node.prev = self.head

        next_node.prev = new_node       #attach neighboring nodes
        self.head.next = new_node

        self.size += 1  #increment the size by one

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)    #create the new node

        prev_node = self.tail.prev  #store the original prev node

        new_node.next = self.tail  #attach the new node 
        new_node.prev = prev_node

        prev_node.next = new_node       #attach neighboring nodes
        self.tail.prev = new_node

        self.size += 1  #increment the size by one
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)

        if index > self.size:
            return
        
        elif index == self.size:
            self.addAtTail(val)
            return 
            
        else:
            new_node = ListNode(val)
            curr = self.head.next
            for _ in range(index):

                curr = curr.next

            prev_node = curr.prev

            new_node.next = curr
            new_node.prev = prev_node

            prev_node.next = new_node
            curr.prev = new_node

            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:

        if index >= self.size or index < 0:
            return 
        else:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
            
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            
            self.size -= 1
            
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)