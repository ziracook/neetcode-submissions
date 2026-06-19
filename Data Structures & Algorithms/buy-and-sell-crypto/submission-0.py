class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        b = 0 # Buy 
        s = 1 # Sell

        while s < len(prices):
            if prices[b] < prices[s]:
                best = max(best, prices[s] - prices[b])
            else:
                b = s
            s += 1
        
        return best

        