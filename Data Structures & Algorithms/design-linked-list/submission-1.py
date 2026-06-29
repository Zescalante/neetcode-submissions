class ListNode:
    # doubly linked ListNode class
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        
        self.head = ListNode() #sentinal head and tail to handle edge cases
        self.tail = ListNode()

        self.head.next = self.tail #Connect the sentinals to start
        self.tail.prev = self.head
        self.size = 0        #variable to track the size of the non-sentinal list

    def get(self, index: int) -> int:
        
        curr = self.head.next #ignore the sentinal head by starting at self.head.next

        if index >= self.size or index < 0: #if index is greater than size of the list
            return -1                       #return -1 as requested

        for _ in range(index):     #otherwise, step through the nodes index times  
            curr = curr.next

        return curr.val             #and return the node's value


    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)    #new node to attach

        next_node = self.head.next  #store the original next node

        new_node.prev = self.head       #place the new_node between sentinal head and original next
        new_node.next = self.head.next

        self.head.next = new_node       #and point the sentinal and original next back to new node, accordingly
        next_node.prev = new_node

        self.size += 1          #increment the size of the linked list

    def addAtTail(self, val: int) -> None:

        new_node = ListNode(val)    

        prev_node = self.tail.prev     #parallel to addAtHead, but now we store the original previous to sentinal tail

        new_node.next = self.tail      #attach the new node in place, between tail and original prev to tail
        new_node.prev = self.tail.prev

        self.tail.prev = new_node      #and point the tail and prev to tail BACK to new node
        prev_node.next = new_node


        self.size += 1      #and increment
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val) #new node to (possibly) insert
        curr = self.head.next   #start at the first actual node

        if index > self.size:   #if index larger than size of the list, just return
            return 
        elif index == self.size: #if the index equals the size of the list
            self.addAtTail(val)  #this is equivalent to just adding at the tail (before the sentinal node of course)
            return
        else:           #otherwise we're inserting somewhere in the middle of the list
            for _ in range(index):  #so step to that location
                curr = curr.next

            prev_node = curr.prev   #since we want to insert BEFORE index i, we store the original previous node

            new_node.prev = prev_node   #attach new node
            new_node.next = curr

            curr.prev = new_node        #and attach neighboring nodes accordingly
            prev_node.next = new_node

            self.size += 1      #increment size by 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next   #start at the first actual node

        if index >= self.size or index < 0:   #return if index out of bounds
            return 

        else:                   #otherwise step through the nodes
            for _ in range(index):
                curr = curr.next
                
            curr.prev.next = curr.next  #point prev node to ignore current and move directly to next node
            curr.next.prev = curr.prev  #and reverse

            self.size -= 1      #decrement size by 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)