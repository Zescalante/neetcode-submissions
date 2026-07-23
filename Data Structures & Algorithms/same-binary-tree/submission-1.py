# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
# PRACTICING BFS
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #to start, if both have no nodes
            return True     #then they're the same

        q1, q2 = deque(), deque()   #initialize queues for by-level search

        q1.append(p)    # add the first nodes in
        q2.append(q)

        while q1 and q2:    #while the queues are not empty
            for _ in range(len(q1)):    #then loop through length of one of them

                node1 = q1.popleft()    #get the leftmost nodes
                node2 = q2.popleft()

                if not node1 and not node2: #if both are none, then just move to next nodes
                    continue 

                #if there's a mismatch, then False
                if (not node1 and node2) or (not node2 and node1) or \
                (node1.val != node2.val):
                    return False

                #if we make it here, the we can add the left and right children to the queues
                q1.append(node1.left)
                q1.append(node1.right)
                q2.append(node2.left)
                q2.append(node2.right)
            
        return True #if we break out of the loop successfully, then the trees are the same
            

# time: O(n)
# space: O(n)