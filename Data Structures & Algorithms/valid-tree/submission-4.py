class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        if not edges and n > 1:
            return False
        
        adjlist = defaultdict(list)
        
        for fm, to in edges:
            # if fm not in adjlist:
            #     adjlist[fm] = []
            # if to not in adjlist:
            #     adjlist[to] = []
            adjlist[fm].append(to)
            adjlist[to].append(fm)
        
        seen = set()
        
        def dfs(node, parent):
        
            if node in seen: 
                return
            
            seen.add(node)
            for neighbor in adjlist[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
        
        dfs(0, -1)
        
        return len(seen) == n
# time: O(V+E) 
# space: O(V+E) 