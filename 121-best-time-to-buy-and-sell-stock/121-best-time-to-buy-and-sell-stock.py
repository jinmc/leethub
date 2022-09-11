class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0
        low = high = prices[0]
        for i in range(len(prices)):
            this_price = prices[i]
            if this_price < low:
                low = this_price
            elif this_price > high:
                high = this_price
            result = max(result, this_price - low)
        return result