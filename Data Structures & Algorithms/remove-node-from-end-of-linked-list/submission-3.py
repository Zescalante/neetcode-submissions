# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, ListNode(0)  #fast pointer to move n ahead of slow
        slow.next = head    #slow acts as a dummy 

        dummy = slow    #set dummy to slow so we can return at the end

        for _ in range(n):  #first move fast n ahead of slow
            fast = fast.next

        while fast: #then, while fast is not None
            fast = fast.next    #move both ahead by one
            slow = slow.next
        slow.next = slow.next.next  #slow.next has the node to remove

        return dummy.next   #finally, return dummy.next to get the new head
    
# time: O(n)
# space: O(1)


