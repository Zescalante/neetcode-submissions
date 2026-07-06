from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        queue = deque()     #initialize queue to hold nodes to process

        if not root:        #if the input root is None
            return []       #return an empty list
        
        res = []
        queue.append(root)  #otherwise we add the root node to the queue

        while len(queue) > 0:       #while there's nodes in the queue to process    
            for i in range(len(queue)):     #loop n times (# of nodes in queue)
                curr = queue.popleft()      #load the front node into curr, to process
                if curr.left:               #if curr has left child
                    queue.append(curr.left) #then add it to tail of queue
                if curr.right:              #and same for right child
                    queue.append(curr.right)
            if curr:                    #if the current node is non-null
                res.append(curr.val)    #curr has the most recent node, which is the rightmost node. So append val to result arr

        return res      #return the final array of node values

# time: O(n)
# space: O(n)
