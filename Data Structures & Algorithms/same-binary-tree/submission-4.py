from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
        #BFS on each tree. q1 and q2
        # if one node is None, or both have values and they are not equal, then immediate False

        if (not p) and (not q): #edge case if both are None from the start. Still identical
            return True 
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False

        q1, q2 = deque(), deque()   #else we make the queues and add the head nodes
        q1.append(p), q2.append(q)

        while q1 and q2:   
            for _ in range(len(q1)):   #standard BFS search
                node1, node2 = q1.popleft(), q2.popleft()

                if not node1 and not node2: #either node could be none. If both are None, that's fine
                    continue
                #or, if only one node is none, or their values don't match, then return False
                if (not node1) or (not node2) or (node1.val != node2.val):
                    return False

                q1.append(node1.left) #otherwise we add the l/r children the queues and continue. 
                q1.append(node1.right) #adding None nodes is fine
                q2.append(node2.left)
                q2.append(node2.right) 

        return True

# time: O(n)
# space: O(n)