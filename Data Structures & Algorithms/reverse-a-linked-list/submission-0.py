# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head.next.val)
        prev = None
        while head:
            # curr = head
            next_node = head.next

            # curr.next = prev
            head.next = prev
            # head.next = head
            # prev = prev.next
            prev = head
            head = next_node
            # head.next, head = head, head.next
            # head = head.next
            # prev = 

            # head = head.next
        return prev