class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ONE POINTER ARRAY AND UPDATING PROFIT VARIABLE?

        min_buy_val = prices[0]
        best_prof = 0

        for i in range(len(prices)):    #this is selling inx
            # buy_ind = max(prices[i] - prices[buy_ind], prices[buy_ind])
            # if prices[i] - min_buy_val > 
            min_buy_val = min(min_buy_val, prices[i])
            best_prof = max(prices[i] - min_buy_val, best_prof)
        
        return best_prof


            




        