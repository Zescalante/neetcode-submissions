# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isbalanced = True

        def dfs(node):

            if not node:
                return 0

            leftHeight, rightHeight = dfs(node.left), dfs(node.right)

            if abs(leftHeight - rightHeight) > 1:
                self.isbalanced = False
                # return False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.isbalanced


# time: O(n)
# space: O(n)