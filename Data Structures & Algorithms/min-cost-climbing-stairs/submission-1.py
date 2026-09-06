class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp top down memoization
        visited = [-1]*len(cost) #initialize arr with same number of steps as cost arr
        def dfs(i): #dfs with with stair index i
            if i >= len(cost): return 0 #if we reach top of stairs, return 0

            if visited[i] != -1:    #if we've already visited this step, return the cost
                return visited[i]
            # otherwise, update the stair cost at i 
            visited[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))  

            return visited[i]   #and return the cost at i 
 
        return min(dfs(0), dfs(1))

# time: O(n)
# space: O(n)