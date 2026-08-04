# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root.left and not root.right:
            return 0

        max_diam = 0

        def dfs(node):
            nonlocal max_diam
            if not node:
                return 0

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            max_diam = max(leftHeight + rightHeight, max_diam)

            return max(leftHeight, rightHeight) + 1

        dfs(root)
        return max_diam

# time: O(n)
# space: O(n)