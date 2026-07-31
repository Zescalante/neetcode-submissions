class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #edge cases
        if not n:   #empty tree still counts as a tree
            return True

        if len(edges) != n - 1: #A valid tree must be exactly n-1 edges for n nodes
            return False

        if not edges and n > 1: #if there's no edges but more than one node, then not valid
            return False
        
        adjlist = defaultdict(list) #adjacency list to document node connections
        
        for fm, to in edges:
            adjlist[fm].append(to)  #undirected connections
            adjlist[to].append(fm)  #so connections go both ways
        
        seen = set() #set to store seen nodes

        def dfs(node, parent):  #we need to track the node and it's "prev" or parent
        
            if node in seen: #if we've seen this node, then return because we found cycle
                return
            
            seen.add(node)  #otherwise we add the new node
            
            #and recurse will all neighbors that aren't current node
            for neighbor in adjlist[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
        
        dfs(0, -1)  #run dfs start node 0 and parent -1 (since -1 is out of range of nodes)
        
        return len(seen) == n   #now check if all nodes have been visited, If yes, then True
# time: O(V+E) 
# space: O(V+E) 