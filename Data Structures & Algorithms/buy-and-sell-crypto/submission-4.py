class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0
        min_price = prices[0]

        while l<len(prices):
            min_price=min(min_price, prices[l])
            if prices[l]-min_price > max_profit:
                max_profit = prices[l]-min_price
            l+=1
        return max_profit


        
        
        

        