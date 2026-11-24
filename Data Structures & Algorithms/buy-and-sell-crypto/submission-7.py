class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        # l = buy, right = sell
        maxP = 0
        while r < len(prices):
            # any sale you make if prices[r] , prices[l], would mean that prices [r] is less than or equal too so using prices[r] as pointer will help sell
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

        