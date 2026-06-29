# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # I want to implement using recursion
        if not head or not head.next: #base case: if head is None or no head.next, then return the head 
            return head

        new_head = self.reverseList(head.next)  #recursive step. Make a new_head with head.next as the head. This is the reversed sublist's head
        head.next.next = head   #point the next node back to current node?
        head.next = None        #disconnect the old head 

        return new_head