# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS. kth smallest, so in-order? left->current->right
        self.count = 0  #keep track of nodes we've processed
        self.res = 0    #store the result value
        def dfs(node):  

            if not node:    #if no node, the return nothing
                return None

            dfs(node.left)  #in-order, so left first

            self.count += 1 #then increment count

            if k == self.count: #if we've hit the node count (k-th smallest)
                self.res =  node.val    #then we found the answer
                return  #break out of dfs
                
            dfs(node.right)  #finally, search right

        dfs(root)   #run dfs
        return self.res #and return the result

# time: O(n)
# space: O(n)