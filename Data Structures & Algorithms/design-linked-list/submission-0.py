class ListNode:

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        #i want to implement a doubly linked list
        self.tail = ListNode(0)
        self.head = ListNode(0)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        dummy = self.head.next #store the head in a dummy. Set it to head.next since we want to count starting at actual first node

        if index >= self.size:  #If the index is equal to or greater than the size of the linked list
            return -1           #return -1 as requested 
        for i in range(index):  #loop through (index) number of times
            dummy = dummy.next  #keep moving through the list

        return dummy.val        #return the value of the node at the index!

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val) #creating new node

        # If we're inserting new node between A->B:
        A = self.head           #store the original head node
        B = self.head.next      #and store the original successor of the head node

        new_node.prev = A       #place the new node after the original head
        A.next = new_node       #and point the next node of the head to the new node

        new_node.next = B       #place the new node before original successor node
        B.prev = new_node       #and point the previous node of the successor back to the new node

        self.size += 1          #increment the size of the linked list by one


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val) #creating new node

        # If we're inserting new node between A->B(original tail):
        B = self.tail           #store the original tail node
        A = self.tail.prev      #and store the original previous of the tail node

        new_node.next = B       #place the new node before the original tail
        B.prev = new_node       #and point the original tail back to new node

        new_node.prev = A       #place the new node after original previous node
        A.next = new_node       #and point the original previous node of tail back to the new node

        self.size += 1          #decrement the size of the linked list by one

        

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = self.head
        new_node = ListNode(val)

        if index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return 
        else:
            for i in range(index):
                dummy = dummy.next

        
            # If we're inserting new node between A->B:
            A = dummy           #store the original head node
            B = dummy.next      #and store the original successor of the head node

            new_node.prev = A       #place the new node after the original head
            A.next = new_node       #and point the next node of the head to the new node

            new_node.next = B       #place the new node before original successor node
            B.prev = new_node       #and point the previous node of the successor back to the new node

            self.size += 1          #increment the size of the linked list by one
            
        


    def deleteAtIndex(self, index: int) -> None:
        dummy = self.head.next
        # new_node = ListNode(val)

        # if index == self.size:
        #     self.addAtTail(val)
        if index >= self.size:
            return 
        else:
            for i in range(index):
                dummy = dummy.next

            # we're deleting node B between A->B->C:
            A = dummy.prev           #store the original head node
            B = dummy               #and store the original successor of the head node
            C = dummy.next

            A.next = C       #and point the next node of the head to the new node
            C.prev = A

            # new_node.next = B       #place the new node before original successor node
            # B.prev = new_node       #and point the previous node of the successor back to the new node

            self.size -= 1          #increment the size of the linked list by one



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)  