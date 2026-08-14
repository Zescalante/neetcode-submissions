# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1, l2 list vals stode in reverse order, i.e. ones->tens->hundreds
        # for each node we sum the l1,l2 val, place remainder (%) in the node,
        # and carry tens (//) to next
        # we loop until the short list runs out. so while l1 AND l2

        dummy = ListNode(0) #listnode to return the head of the final LL
        carry = 0   #initialize the carry
        curr = dummy   #set the current node pointer

        while l1 or l2: #we want to look at all nodes, even if one runs out
            
            val1 = 0 if not l1 else l1.val  #if one list runs out, we just use fill-in zeros
            val2 = 0 if not l2 else l2.val

            tot = val1 + val2 + carry   #find the total
            carry = tot // 10   #the carry moves to the next node
            remainder = tot % 10    #the remainder is placed in the next node

            curr.next = ListNode(val = remainder)   #create the next node, with the remainder filled in 

            curr = curr.next    #step the LL forward
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry != 0:  #if there's still carry at the end
            curr.next = ListNode(val=carry) #just make a new node for it 

        return dummy.next


# time: O(n + m); n, m = lengths of linked lists
# space: O(1)