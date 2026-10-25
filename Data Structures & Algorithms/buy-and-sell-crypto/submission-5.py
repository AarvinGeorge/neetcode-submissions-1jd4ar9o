# Dynamic programming and. greedy algorithm
# This algorithm works because you are given the history upfront
# Time complexity :  O(n) || Space Complexity : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return maxP