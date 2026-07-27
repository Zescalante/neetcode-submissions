# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # take a node from each
        # sorted in reverse so we can go in order. 1s place, 10s place,...
        # need to store each sum in a new node, and carry the remainder to 
        # the next. So x + y // 10 carrys to the next 

        res = ListNode() #initialize a dummy
        carry = 0        #start a carry counter

        curr = res      #get the "current" node 
        while l1 or l2: #while either l1 or l2 still has nodes to search

            #then we get their values if they exist, or zero if they don't
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            #sum the node values with the carry
            tot = val1 + val2 + carry
            carry = tot // 10   #update the carry from the total
            
            new_node = ListNode(tot % 10)   #a new node will hold the remainder
            curr.next = new_node        #attach the new node

            l1 = l1.next if l1 else None    #move l1/l2 along
            l2 = l2.next if l2 else None 
            curr = curr.next            #and step current node forward
        
        if carry != 0:      #after the loop, if there's still a remainder
            curr.next = ListNode(carry) #then we just attach it in a new node
        
        return res.next     #we turn res.next to get the head of the new linked list

# time: O(m + n)
# space: O(1) since we dont count solution space