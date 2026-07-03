# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #helper function to mind the minimum child node of the input root
    def findMinValNode(self, root: Optional[TreeNode]):
        curr = root        #set the current node
        while curr and curr.left:   #while the current node AND its left child exists
            curr = curr.left        #then continue stepping through the left child nodes
        return curr             #once we've reached the end, return the current node

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:        #if there's no current root to look at
            return None     #return None
        
        if key > root.val:  #if the key is greater than current node value,
            root.right = self.deleteNode(root.right, key)    #recurse by passing root.right into deleteNode with the key

        elif key < root.val:     #and if key is smaller
            root.left = self.deleteNode(root.left, key)  #recursive call with root.left
        
        else:       #else if the key is equal to the current node value
            if not root.left:    #and if there's no left child
                return root.right   #then return the right child
            elif not root.right:    #or vice versa
                return root.left
            else:   #else, there's two child nodes
                minNode = self.findMinValNode(root.right) #so we need to find the right child node with the minimum value
                root.val = minNode.val  #set the current node's value to the minimum value
                root.right = self.deleteNode(root.right, minNode.val) #and we step into right child to find and delete the minimum-value node

        return root     #finally we return the root of the BST, now without the node having the key

