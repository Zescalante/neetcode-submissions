#DP. MEMOIZATION
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # we want to keep track of number of ways to reach the amount
        seen = {} #storing previously-seen states and their count of ways to reach target. Here, it's the index and current sum

        def dfs(i, tot):

            if (i, tot) in seen:           #if the state has been seen
                return seen[(i, tot)]      #just return the number of ways from that state  

            if tot > amount or i == len(coins): #or, if we've exceeded the amount or hit the end of the list                
                return 0        #no contriubtion 
            
            if tot == amount:   #otherwise, if we're at the total
                return 1        #then this counts as one way

            #we store the current store by adding dfs with the next element an same total (skipping this one)
            #or taking adding the current coin again
            seen[(i, tot)] = dfs(i + 1, tot) + dfs(i, tot + coins[i])

            return seen[(i, tot)] #we return the number of ways to met target from state (i, tot)

        #run with starting index 0 and current total 0
        return dfs(0,0)

# time: O(n*a); n = number of coins, a = target value
# space: O(n*a); n = number of coins, a = target value
