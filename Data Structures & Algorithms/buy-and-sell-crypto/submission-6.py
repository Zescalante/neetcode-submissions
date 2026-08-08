class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0] #initialize first buy to the first day's price
        max_prof = 0    #initialize profit to 0 
    
        for sell in prices: #possible sell value
            curr_prof = sell - buy  #then calculate the profit if we decide to sell on this day
            max_prof = max(max_prof, curr_prof) #finally, update the maximum profit achieved so far
            buy = min(buy, sell)    #calculate the lowest buy price so far
            
        return max_prof

# time: O(n)
# space: O(1)