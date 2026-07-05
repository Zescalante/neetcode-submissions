# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0      #make a counter as an attribute of the class to update 
        self.res = None     #make a variable to store the result

        # inorder dfs is perfect to find k-th smallest value
        def dfs(node):
            if not node:    #if the node is empty/not there
                return      #just step out  

            dfs(node.left)  #recursive call to the left node until we find the smallest val
            self.count +=1  #increment the counter by one

            if self.count == k:     #if we've found the kth smallest value
                self.res = node.val #then update the result and return it 
                return 

            dfs(node.right)     #otherwise step in the right node to see the next largest value

        dfs(root)   #outside of the helper function, just call the function with the root node

        return self.res #return the resulting kth smallest value!

# time: O(n) n is number of nodes in the BST
# space: O(h) h is height of the BST
