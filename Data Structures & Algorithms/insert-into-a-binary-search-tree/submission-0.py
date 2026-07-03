# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:                #if the current root is Null
            return TreeNode(val)    #then we've passed the leaf and found the location, so make a new node and return 

        if val > root.val:      #if the value is larger than the current node's val
            root.right = self.insertIntoBST(root.right, val)    #then we move into the right branch and insert there recursively

        elif val < root.val:    #if the value is smaller than the current node's val
            root.left = self.insertIntoBST(root.left, val)      #then we move into the left branch and insert there recursively

        #It's guaranteed that val does not exist in the original BST, so no need for an else statement
        return root     #return the root of the updated BST
