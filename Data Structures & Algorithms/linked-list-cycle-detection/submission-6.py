# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # HASHSET SOLUTION 
        visits = set()

        while head and head.next:
            if head in visits:
                return True
            visits.add(head)
            head = head.next

        return False