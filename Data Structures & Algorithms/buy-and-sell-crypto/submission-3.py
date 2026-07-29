class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # must buy before you can sell. Buy low, sell high
        max_profit = 0
        min_buy = prices[0]
        for i in range(len(prices)):
            min_buy = min(prices[i], min_buy)
            # sell_price = prices[i]
            curr_profit = prices[i] - min_buy
            max_profit = max(curr_profit, max_profit)
        
        return max_profit

# time: O(n)
# space: O(1)