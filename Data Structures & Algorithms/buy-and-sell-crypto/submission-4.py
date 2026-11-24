class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            smallest = min(prices[i], smallest)
            
            val = prices[i] - smallest
            profit = max(profit, val)
        return profit

        