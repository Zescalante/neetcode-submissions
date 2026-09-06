class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp top down memoization
        visited = [0]*len(cost)
        def dfs(i):
            if i >= len(cost): return 0

            if visited[i] != 0:
                return visited[i]

            visited[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return visited[i]
 
        return min(dfs(0), dfs(1))

# time: O(n)
# space: O(n)