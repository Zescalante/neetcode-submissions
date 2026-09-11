# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, node1, node2):
        if not node1 and not node2: return True 

        elif node1 and node2 and node1.val == node2.val:
            return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)

        else: return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        # return self.sameTree(root, subRoot)
        
        # if node.left: 
        #     return self.isSubtree(root.left, subRoot) 

        # if node.right: 
        #     return self.isSubtree(root.right, subRoot) 

        return self.sameTree(root, subRoot) or \
        self.isSubtree(root.left, subRoot) or \
        self.isSubtree(root.right, subRoot) 

        # return self.isSubtree(root)
# time: O(m*n); n = nodes in root, m = nodes in subRoot
# space: O(m + n)