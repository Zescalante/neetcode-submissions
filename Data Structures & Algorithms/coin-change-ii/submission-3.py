class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        seen = {}
        # counting the distinct ways to reach the target
        def dfs(i, tot):

            if (i, tot) in seen:
                return seen[(i, tot)]

            if tot > amount or i == len(coins):
                return 0

            if tot == amount and i < len(coins):
                return 1
            
            seen[(i, tot)] = dfs(i, tot + coins[i]) + dfs(i + 1, tot)

            return seen[(i, tot)]
        
        return dfs(0, 0)