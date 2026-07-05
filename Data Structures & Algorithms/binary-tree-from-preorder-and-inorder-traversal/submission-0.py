# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #inorder: dfs where root is processed in-order (left, root, right)
        #preorder: dfs where root is processed before the left and right (root, left, right)
        
        # optimal dfs method
        indices = {val: idx for idx, val in enumerate(inorder)} #dictionary (hashmap) to store inorder list elements

        self.pre_index = 0 #initialize attribute for preorder index as 0

        def dfs(left, right):   #helper function to implement dfs
            if left > right:           #if the left pointer has crossed the right
                return          #then just exit and return None

            root_val = preorder[self.pre_index] #get the current root value using the current preorder index
            self.pre_index += 1     #then increment index by 1
            root = TreeNode(root_val)   #create a tree node with the current root value 
            mid = indices[root_val]     #get the index from the hashmap for the current root_val 
            root.left = dfs(left, mid - 1) #recursively perform dfs with left and mid - 1 indices
            root.right = dfs(mid + 1, right) #recursively perform dfs with right on the other side
            return root             #finally, return the root node

        return dfs(0, len(inorder) - 1)     #then call the function for the full length of the given input lists

