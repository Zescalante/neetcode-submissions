# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:                #if there's no passed-in root, or we're at a leaf node
            return TreeNode(val)    #return the new tree node
        
        if val > root.val:      #if the new value is larger than current node's value
            root.right = self.insertIntoBST(root.right, val)    #we recurse into right branch
        elif val < root.val:    #and vice versa
            root.left = self.insertIntoBST(root.left, val)
        return root             #return the root at the end
        
