from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()    #queue to hold the nodes we'll process at each level

        res = []           #array to hold the subarrays with node values

        if root:           #if the input root is not None
            queue.append(root)  #add the root node to the queue
         
        while len(queue) > 0:           #while there's nodes in the queue to process
            subres = []                 #subarray to hold the current level's node values
            for i in range(len(queue)): #iteration for length of queue
                curr = queue.popleft()  #pop from the queue and store the node in curr
                subres.append(curr.val) #append the current node's value to subres array
                if curr.left:           #if the node has a left child
                    queue.append(curr.left) #add the left child to back of queue
                if curr.right:           #if node has right child
                    queue.append(curr.right) #add right child to back of queue

            res.append(subres)      #append the subarrary to the final result array
        
        return res      #return the final array

# time: O(n)
# space: O(n)


        