# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast and slow pointers. Then reversing linked list

        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # slow.next is now the head of second half. original head is start of first half
        back_half = slow.next

        # after storing back half, set slow.next to none to cut it off
        slow.next = None

        # now reverse back_half 
        prev = None
        curr = back_half
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        l1, l2 = head, prev #just renaming for clarity

        while l1 and l2:
            next_l1, next_l2 = l1.next, l2.next

            l1.next = l2
            l2.next = next_l1

            l1, l2 = next_l1, next_l2

        

# time: O(n)
# space: O(1)