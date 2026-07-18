# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #DEPTH-FIRST SEARCH
        # POST-ORDER TRAVERSAL?
        if not root:        #if the input is None, then stop early
            return None

        def reverse(node):  #helper function to swap left and right children
            node.left, node.right = node.right, node.left

        def postorder(node):    #we want postorder, since we want to process both children before the parent
            if not node:        #base case
                return

            postorder(node.left)    #postorder arrangement: left, right, and then the node itself
            postorder(node.right)
            reverse(node)

            return node             #this will eventually return the root
        
        return postorder(root)

# time: O(n)
# space: O(h); h = height of tree
        