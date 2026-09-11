# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, node1, node2):   #check if two input trees are identical
        if not node1 and not node2: return True     #if both nodes are None, that's ok

        elif node1 and node2 and node1.val == node2.val:    #or if both exist and same vals, check their children
            return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)

        else: return False  #otherwise there's a mismatch so False (not the same tree)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True #if no subRoot to compare, then automatic True
        if not root: return False #if no curret node, then return False
        #either the current subtree is identical to subRoot, or the left or right child trees are. Any is fine
        return self.sameTree(root, subRoot) or \
        self.isSubtree(root.left, subRoot) or \
        self.isSubtree(root.right, subRoot) 

# time: O(m*n); n = nodes in root, m = nodes in subRoot
# space: O(m + n)