"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:    #if no node in the first place, return none
            return None
        
        adjlist = {}    #dictionary to map the old to the new 

        def dfs(node):

            if node in adjlist:         #if node already in hashmap, then already been cloned
                return adjlist[node]    #so return that clone
             
            copy = Node(node.val)   #else, we create a copy (clone) of the node
            adjlist[node] = copy    #and map the copy to the original map

            for neighbor in node.neighbors:     #we also have to map copies of its neighbors 
                neighbor_clone = dfs(neighbor)  #we have to append the neighbor copies 
                copy.neighbors.append(neighbor_clone)

            return copy
    
        return dfs(node)

# time: O(E + V) = O(n)
# space: O(V)