# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:       #if there's no root, then there's no depth
            return 0

        q = deque()     #initialize q 
        q.append(root)  # add the root to the queue
        depth = 0       #and initialize the depth

        while len(q) > 0:       #while the queue is not empty
            for i in range(len(q)): #loop through the nodes that were in the queue before appending any more
                curr = q.popleft()  #pop the node from the left (FIFO)
                if curr.left:       #if has a left child then append it to back of queue
                    q.append(curr.left)
                if curr.right:      #and same for right
                    q.append(curr.right)
            depth += 1              #at the end, we've cleared the whole level, so increment depth
        return depth                #return the depth at the end

# time: O(n)  since we have to look at all of the nodes
# space: O(n) since we have to append all of the nodes