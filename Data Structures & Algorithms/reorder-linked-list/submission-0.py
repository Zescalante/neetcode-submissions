# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head 

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # second_half_head = slow.next
        # slow.next = None

        # we now have midpoint. Fast is at end. now reverse second half
        prev = None
        curr = slow.next 
        slow.next = None

        while curr:
            next_node = curr.next 
            curr.next = prev

            prev = curr
            curr = next_node
        # prev is now head of reversed second half

        first, second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1
            first, second = temp1, temp2

    
    



            
