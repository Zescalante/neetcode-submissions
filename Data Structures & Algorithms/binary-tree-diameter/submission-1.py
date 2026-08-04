# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diam = 0    #diameter result variable to update within dfs

        def dfs(node):
            nonlocal max_diam   #import max_diam
            if not node:    #if there's no node 
                return 0    #then no contribute

            leftHeight = dfs(node.left) #dfs with left and right
            rightHeight = dfs(node.right)
            # update max_diam to sum of returned dfs calls if it's larger
            max_diam = max(leftHeight + rightHeight, max_diam)
            
            #we return HEIGHT here. The max of either left of right PLUS ONE FOR HEIGHT
            return max(leftHeight, rightHeight) + 1

        dfs(root)   #call the function
        return max_diam

# time: O(n)
# space: O(n)