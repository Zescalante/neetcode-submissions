# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # helper function with is essentially postorder dfs
    def get_height(self, node: Optional[TreeNode]):

        if not node:    #if no node to check height of
            return 0    #then the height is zero

        left = self.get_height(node.left)      #recursively grab the values in the left 
        right = self.get_height(node.right)    #and right sub branches

        #if the height difference exceeds 1 OR left or right values are -1
        if abs(left - right) > 1 or left ==  -1 or right == -1:
            return -1      #then flag the branch by returning -1

        return 1 + max(left, right)     #otherwise, return the height of the subtree

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:        #if no root to check
            return True     #then we define the tree as balanced. Return True

        return self.get_height(root) != -1     #run the dfs function. If it returns -1, then False. Else True
        
# time: O(n)
# space: O(h) 