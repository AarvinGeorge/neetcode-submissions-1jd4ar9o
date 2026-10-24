# brute force Check all possible buy-sell pair
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        for i in range(len(prices)):
            buyPrice = prices[i]
            for j in range(i+1,len(prices)):
                sellPrice = prices[j]
                result = max(result, sellPrice - buyPrice)
            
        return result