class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                maximum = max(profit, maximum)
        return maximum
                

            
            

        