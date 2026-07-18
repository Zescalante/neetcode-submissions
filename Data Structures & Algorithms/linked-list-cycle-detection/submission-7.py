# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # HASHSET SOLUTION 
        visits = set()  #initialize a set to hold seen nodes

        while head and head.next:   #while the current node is not none, and there's a next node
            if head in visits:      #check if node has been seen
                return True         #if yes, then we have a cycle. Return True  
            visits.add(head)        #otherwise, add the node to the set
            head = head.next        #and step to next node

        return False                #if we're out of the loop, then we've hit an end. No cycle. Return False

# time: O(n)
# space: O(n)