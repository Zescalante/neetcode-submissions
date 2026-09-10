class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        seen = {}

        def dfs(i):
            if i in seen:
                return seen[i]

            if i >= len(cost):
                return 0

            seen[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return seen[i]

        return min(dfs(0), dfs(1))