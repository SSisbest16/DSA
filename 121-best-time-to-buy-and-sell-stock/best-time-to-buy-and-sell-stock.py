class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, p = 0, 1, 0
        while r < len(prices):  
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                p = max(profit, p)
            else:
                l = r  
            r += 1 
        return p
        