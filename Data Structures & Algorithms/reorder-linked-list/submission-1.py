# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Fast and slow pointers will find the midpoint. 
        slow, fast = head, head 

        #as long as there's a fast node and a next node to step into
        #then increment slow by one and fast by two
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # we now have midpoint. Fast is at end of second half.
        # slow.next is the head of the second half
        curr = slow.next 
        slow.next = None

        #prev is a dummy to point back to
        prev = None
        while curr:
            next_node = curr.next #store curr's next node
            curr.next = prev      #then point curr backwards

            prev = curr         #move prev forward
            curr = next_node    #move curr forward

        # prev is now head of reversed second half

        # declaring first and second for clarity
        first, second = head, prev
        
        # now we interweave them
        while second:
            temp1, temp2 = first.next, second.next  #store the next pointers
            first.next = second     #then point first to second
            second.next = temp1     #and second to first's next
            first, second = temp1, temp2    #and move both forward

# time: O(n)
# space: O(1)



            
