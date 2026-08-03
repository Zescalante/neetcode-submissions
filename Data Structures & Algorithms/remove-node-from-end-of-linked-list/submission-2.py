# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, ListNode(0)
        slow.next = head

        dummy = slow
        # if not head.next:
        #     return None

        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next

        # while first:
        #     for _ in range(n):
        #         first = first.next
        #     second = second.next
        # second.next = second.next.next


        # if not head.next:
        #     return None
        # curr = head
        # # first find end of ll
        # slow, fast = head, head.next

        # size = 2
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next
        #     size += 2 

        # # if (size - n) > (size - 1) // 2 :    #compare target node index to size of ll 
        # #     # if true, then search from middle (slow)
        # #     for _ in range():
        # #         slow = slow.next 
        
        # #     #slow.next is now the node to detach 
        # #     slow.next = slow.next.next
        # # else: #else we start from the front to detach
        # #     for _ in range():
        # #         head = head.next 
        # #     head.next = head.next.next
            
        # print(size, n)
        # print(size - n)
        # dummy = head
        # for _ in range(size - n - 1):
        #     head = head.next
        # head.next = head.next.next
        # # print(head.val)
        # return dummy


