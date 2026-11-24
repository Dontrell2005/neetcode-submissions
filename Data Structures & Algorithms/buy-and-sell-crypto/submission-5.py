class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        l,r = 0, 1
        while r < len(prices):
            fit = prices[r] - prices[l]
            if fit > 0:
                profit = max(profit, fit)
            else:
                l = r
            r += 1
        return profit


        