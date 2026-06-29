# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #initialize a previous node as None, to point the others to
        curr = head #place current head into curr

        while curr:     #while there's still a "current" node to look at
            next_node = curr.next   #place the next node into a placeholder variable. So we don't lose the connection
            curr.next = prev        #point curr's next node in the other direction
            prev = curr             #move prev node one forward
            curr = next_node        #move the current node one forward

        return prev                 #at the end, the prev node is now the new head
# time: O(n)
# spac: O(1)  