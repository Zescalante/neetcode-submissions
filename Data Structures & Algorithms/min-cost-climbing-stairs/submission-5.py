class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # seen = {}
        seen = [-1]*len(cost)
        def dfs(i):

            if i >= len(cost):
                return 0

            if seen[-1] != -1:
                return seen[i]

            seen[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return seen[i]

        return min(dfs(0), dfs(1))

# time: O(n)
# space: O(n)