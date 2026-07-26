# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = deque(), deque()

        if not p and not q:
            return True

        # if (not p and q) or (not q and p) or (q.val != p.val):
        #     return False

        q1.append(p)
        q2.append(q)

        while q1 and q2:
            for _ in range(len(q1)):

                node1 = q1.popleft()
                node2 = q2.popleft()

                #if both are none, that's still ok
                if not node1 and not node2:
                    continue

                if (not node1 and node2) or (not node2 and node1) or (node1.val != node2.val):
                    return False

                q1.append(node1.left)
                q1.append(node1.right)

                q2.append(node2.left)
                q2.append(node2.right)
                
        return True