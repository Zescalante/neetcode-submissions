# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS. Last entry in every queue fill?
        if not root:    #edge case if no root to begin with
            return []
        q = deque([root])   #create a queue and add the root
        res = []    #list to hold the result
        while q:    #as long as q is non-empty
            for _ in range(len(q)): #go through all nodes in current level
                node = q.popleft()  #get the leftmost node. FIFO
                if node.left:   #if l child, then add
                    q.append(node.left) 
                if node.right:  #same for right 
                    q.append(node.right)
            if node:    #after, the last node's value is target value, so add to result
                res.append(node.val)

        return res
# time: O(n)
# space: O(n)