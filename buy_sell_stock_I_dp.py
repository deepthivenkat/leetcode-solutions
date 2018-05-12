class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_val = prices[0]
        profit = 0
        for i in prices[1:]:
            min_val = min(min_val,i)
            profit = max(profit, i-min_val)
        return profit