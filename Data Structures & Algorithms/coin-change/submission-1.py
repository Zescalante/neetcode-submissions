class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp with memoization
        # amount is the target. Hit the target exactly in fewest coins
        # counting how many coins it takes. Global minimum tracker  

        table = {} #storing seen remaining amount (key) and num coins (val)
        def dfs(remaining): #parameter is remaining amount
            if remaining in table: return table[remaining]  #if already in table, return that

            if remaining == 0:  #if we hit the target, then no more coins needed
                return 0
            if remaining < 0:   #if we overshot the target, return as infinity
                return float('inf')

            res = float('inf')  #initialize as infinity
            for coin in coins:  #iterate through the coins
                if remaining - coin >= 0:   #if we can safely subtract the value from remaining
                    res = min(res, 1 + dfs(remaining - coin))   #then update res

            table[remaining] = res  #store in the table 
            return res  # and return the res

        result = dfs(amount)    #run dfs
        return result if result != float('inf') else -1 #if result not infinity, then return result

# time: O(n*t); n = length of coins, t = amount
# space: O(t) 