class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        min_val = prices[0] if prices else 0
        for price in prices:
            if price > min_val:
                profit += price - min_val
                min_val = price
            min_val = price
        return profit