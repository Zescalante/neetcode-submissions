# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # post-order DFS
        self.max_sum = root.val

        def dfs(node):
            if not node:
                return 0
            
            leftsum, rightsum = dfs(node.left), dfs(node.right)

            #update best path through this node
            curr_sum = node.val + max(0, leftsum) + max(0, rightsum)
            self.max_sum = max(curr_sum, self.max_sum)

            # return best extendable downward path
            return node.val + max(0, leftsum, rightsum)

        dfs(root)
        return self.max_sum 

# time: O(n)
# space: O(n)





# time: O(n)
# space: O(n)
        