"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        #build the adjacency list
        adjlist = {}

        def dfs(node):
            if node in adjlist:
                return adjlist[node] 
             
            copy = Node(node.val)
            adjlist[node] = copy

            for neighbor in node.neighbors:
                # adjlist[copy].append(neighbor)
                neighbor_clone = dfs(neighbor)
                copy.neighbors.append(neighbor_clone)

            return copy
        
        # dfs(node)
        return dfs(node)

