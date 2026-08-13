# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #dummy to return as result head
        curr = dummy    #current pointer for attaching nodes

        while list1 and list2:  #while both lists have nodes (we need nodes to compare)
            if list1.val <= list2.val:  #if list1 has smaller val, then 
                curr.next = list1   #that's where curr will point
                list1 = list1.next  #and move list1 along
            else:   #otherwise list2 has smaller value
                curr.next = list2
                list2 = list2.next
            curr = curr.next    #then step curr along for next attaching point

        curr.next = list1 or list2 #attach any remaining nodes

        return dummy.next

# time: O(n + m)
# space: O(1)
