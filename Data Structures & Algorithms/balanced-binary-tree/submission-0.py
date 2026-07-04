# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height(self, node: Optional[TreeNode]):

        if not node:
            return 0

        left = self.get_height(node.left)
        right = self.get_height(node.right)

        if abs(left - right) > 1 or left ==  -1 or right == -1:
            return -1

        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.get_height(root) != -1
        
        