# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()  #handles the edge case
        curr = dummy        #holds the current node being worked on

        while list1 and list2:  #while list1 and list2 both still have nodes to check
            if list1.val <= list2.val: #if list1 node has the smaller value
                curr.next = list1       #attach list1 node to curr list
                list1 = list1.next      #and increment list1 node

            else:                  #otherwise, list2 node has smaller value
                curr.next = list2  #so attach it to curr
                list2 = list2.next #and increment list2 node

            
            curr = curr.next    #move the current node along

        curr.next = list1 or list2 #attached the remaining nodes from either list1 or list2, if there's leftover

        return dummy.next #return the head of the sorted linked list!




    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None

        # for i in range(1, len(lists)):  #loop through the number of subarrays, starting at index 1 so we can do i, i - 1


        while len(lists) > 1:

            mergedlists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                #merge two sub-lists and return the head of the resulting list. Store the head in list[i] so it can be checked against the next list!
                # lists[i] = self.mergeTwoLists(lists[i], lists[i - 1]) 
                mergedlists.append(self.mergeTwoLists(l1, l2))
            lists = mergedlists
            
        # return lists[0]
        return mergedlists[0]
