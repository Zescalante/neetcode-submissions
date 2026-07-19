class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ONE POINTER ARRAY AND UPDATING PROFIT VARIABLE
        min_buy_val = prices[0]     #initialize minimum buy price at first day, since we have to buy before selling
        best_prof = 0         #initialize best profit at 0.

        for i in range(len(prices)):   #step through in order
            best_prof = max(prices[i] - min_buy_val, best_prof) #update the best posible profit
            min_buy_val = min(min_buy_val, prices[i])   #if the current day has a lower price for buying, then update
        
        return best_prof

# time: O(n)
# space: O(1)


            




        