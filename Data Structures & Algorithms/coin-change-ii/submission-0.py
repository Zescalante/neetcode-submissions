#DP MEMOIZATION?
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # we want to keep track of number of ways to reach the amount
        seen = {}
        def dfs(i, tot):
            if (i, tot) in seen:
                return seen[(i, tot)]

            if tot > amount or i == len(coins):
                return 0
            
            if tot == amount:
                return 1

            seen[(i, tot)] = dfs(i + 1, tot) + dfs(i, tot + coins[i])

            return seen[(i, tot)]

        return dfs(0,0)
