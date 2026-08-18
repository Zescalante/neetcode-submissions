# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS
        if not root:
            return []
            
        q = deque()
        q.append(root)

        res = []
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                if not node:
                    continue

                if node:
                    level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res

# time: O(n)
# space: O(n)