class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maximum = 0
        # for i in range(len(prices)):
        #     for j in range(len(prices)):
        #         if prices[j] - prices[i] > maximum and j > i :
        #             maximum = prices[j] - prices[i]
        # return maximum
        maximum = 0 
        l = 0
        r = 1
        while r < len(prices):
            if prices[r] > prices[l]:
                maximum = max(prices[r] - prices[l], maximum)
            else:
                l = r
            r = r + 1
        return maximum
                

            
            

        