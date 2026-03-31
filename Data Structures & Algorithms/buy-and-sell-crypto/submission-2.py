class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if prices[j] - prices[i] > maximum and j > i :
                    maximum = prices[j] - prices[i]
        return maximum

            

        