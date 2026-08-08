class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        max_prof = 0
    
        for sell in prices: #possible sell value
            buy = min(buy, sell)
            curr_prof = sell - buy
            max_prof = max(max_prof, curr_prof)
        
        return max_prof

# time: O(n)
# space: O(1)