# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []     #we need an array to store the result

        if not root:        #if the node doesn't exist
                return []   #return an empty list. Don't return None

        #otherwise we return the usual left and right traversal
        #but we're concatenating with a list of the root val in between (for inorder)
        return self.inorderTraversal(root.left) + \
               [root.val] + \
               self.inorderTraversal(root.right)