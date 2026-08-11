class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer = 0
        max_profit = 0
        min_price = prices[0]

        while pointer<len(prices):
            min_price = min(min_price, prices[pointer])
            if prices[pointer]-min_price > max_profit:
                max_profit = prices[pointer]-min_price
            pointer+=1
        return max_profit       