class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        minprice = 999999999999
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > max_profit:
                max_profit = prices[i] - minprice

        return max_profit
