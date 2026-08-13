# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast, slow = head, ListNode(0)  #fast and slow, with slow starting at a dummy node 
        slow.next = head

        dummy = slow #will return dummy.next as the head of result linkedlist

        for _ in range(n):
            fast = fast.next #move fast n ahead of slow

        while fast: #then move fast and slow together to reach the node to remove
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next # slow.next is the node to remove
        
        return dummy.next
# time: O(N)
# space: O(1)