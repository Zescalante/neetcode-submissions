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
        if not root:
            return None

        def reverse(node):
            node.left, node.right = node.right, node.left

        def postorder(node):
            if not node:
                return

            postorder(node.left)
            postorder(node.right)
            reverse(node)

            return node
        
        return postorder(root)
        