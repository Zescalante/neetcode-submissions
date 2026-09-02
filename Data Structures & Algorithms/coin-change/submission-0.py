class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp memoization
        # amount is the target. Hit the target exactly in fewest coins
        # counting how many coins it takes. Global minimum tracker  
        table = {}
        # min_coins = 
        def dfs(remaining):
            if remaining in table: return table[remaining]

            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            res = float('inf')
            for coin in coins:
                if remaining - coin >= 0:
                    res = min(res, 1 + dfs(remaining - coin))

            table[remaining] = res
            return res

        result = dfs(amount)
        return result if result != float('inf') else -1

# time: O(n*t); n = length of coins, t = amount
# space: O(t)