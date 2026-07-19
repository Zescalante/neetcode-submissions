class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ONE POINTER ARRAY AND UPDATING PROFIT VARIABLE?

        #BRUTE FORCE SOLUTION
        max_prof = 0 

        for i in range(len(prices)):    #i is buy index
            for j in range(i + 1, len(prices)): #j is sell index
                max_prof = max(prices[j] - prices[i], max_prof)
        return max_prof
