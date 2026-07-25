class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        seen = {}
        # counting the distinct ways to reach the target
        def dfs(i, tot):

            #first check if state has been seen
            if (i, tot) in seen:    
                return seen[(i, tot)]

            #if not, then check if we've overshot amount or reached end of list
            if tot > amount or i == len(coins):
                return 0

            #if not, then check if we've hit the target
            if tot == amount and i < len(coins):
                return 1
            
            # otherwise, we continue recursion
            seen[(i, tot)] = dfs(i, tot + coins[i]) + dfs(i + 1, tot)

            return seen[(i, tot)]
        
        return dfs(0, 0)