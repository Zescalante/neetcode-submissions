# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:        #if no root
            return False    #return False 

        def leafPath(node, target):     #usual node dfs backtracking structure

            if not node:            #if no current node
                return False        #return False since we hit a dead end

            difference = target - node.val  #subtract the current node's value from the target
            
            if not node.left and not node.right:  #if no children
                return difference == 0            #check if the current difference is 0. If it is, then success and return True
            if leafPath(node.left, difference):   #if there's a left child, enter recursion with the difference as the new target value
                return True                        
            if leafPath(node.right, difference):  #same if there's a right child
                return True

            return False                          #if none of the criteria met, return False

        return leafPath(root, targetSum)        #call the backtracking function with the original root and target value

# time: O(n)
# space: O(n)
            
