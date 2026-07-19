# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DEPTH-FIRST SEARCH
        if not root:    #if there's no current node 
            return 0    #then return a depth of 0
        
        leftDepth = self.maxDepth(root.left)    #
        rightDepth = self.maxDepth(root.right)

        return 1 + max(leftDepth, rightDepth)

# time: O(n)
# space: O(h); h = height of tree
