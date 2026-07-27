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
        # the next. So x + y % 10 carrys to the next 

        res = ListNode()
        carry = 0

        curr = res
        while l1 or l2:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0


            tot = val1 + val2 + carry
            carry = tot // 10
            new_node = ListNode(tot % 10)

            curr.next = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
            curr = curr.next
        
        if carry != 0:
            curr.next = ListNode(carry)
        
        return res.next