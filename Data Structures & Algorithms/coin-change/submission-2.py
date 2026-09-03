class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')]*(amount + 1) #going from 0 to amount. counting from bottom 

        dp[0] = 0 #base: to get amount of 0, it takes 0 coins

        for a in range(1, amount + 1):  #step from bottom (1) to amount
            for c in coins: #now go through our list of coins
                if a - c >= 0:  #if we don't go negative, then keep searching
                    dp[a] = min(dp[a], 1 + dp[a - c])   #remember to update dp arr with miminum

        return dp[amount] if dp[amount] != float('inf') else -1

# time: O(n*t); n = length of coins, t = amount
# space: O(t) 