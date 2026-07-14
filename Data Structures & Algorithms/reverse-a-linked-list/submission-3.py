# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = None
        # curr = head

        # while curr:
        #     next_node = curr.next   #store the next

        #     curr.next = dummy       #reverse the pointer

        #     dummy = curr        #move prev one forward
        #     curr = next_node    #move current node one forward
    

        # return dummy

        #base case: we get to the end of the list
        if not head:
            return None
 
        new_head = head

        if head.next:
            # recursion to reach the other nodes
            new_head = self.reverseList(head.next)
            head.next.next = head
            
        head.next = None

        return new_head

# time: O(n)
# space: O(n)








