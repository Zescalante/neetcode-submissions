class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if numCourses == 0 or prerequisites is None:
            return False
        
        adj = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            adj[course].append(pre)

        visited = set()
        visiting = set()

        def dfs(course):

            if course in visiting:
                return False        #we're in a cycle. return False
            if course in visited:
                return True             #we've checked this one already
            
            visiting.add(course)

            for p in adj[course]:
                if not dfs(p):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in adj:
            if not dfs(course):
                return False
        
        return True