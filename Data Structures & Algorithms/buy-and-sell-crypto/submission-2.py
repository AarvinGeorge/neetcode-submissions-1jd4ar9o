#Pointers buyPoint , sellPoint
# Time complexity : O(n) || Space Complexity : O(1) 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPoint , sellPoint = 0, 1
        maxProfit = 0

        while sellPoint < len(prices):
            if prices[buyPoint] < prices[sellPoint]:
                maxProfit = max(maxProfit, (prices[sellPoint]-prices[buyPoint]) )
            else:
                buyPoint = sellPoint
            sellPoint += 1
        
        return maxProfit
        