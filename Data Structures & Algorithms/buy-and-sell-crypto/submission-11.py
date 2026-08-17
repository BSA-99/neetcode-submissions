class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for r in range(len(prices)):
            min_price = min(min_price, prices[r])
            if prices[r]-min_price > max_profit:
                max_profit = prices[r]-min_price
        return max_profit

        