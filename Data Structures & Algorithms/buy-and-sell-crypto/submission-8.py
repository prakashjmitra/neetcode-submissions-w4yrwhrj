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
        r = l + 1
        minimum = prices[0]
        for i in range(1,len(prices)):
            minimum = min(minimum,prices[i-1])
            if prices[i] - minimum > maximum:
                maximum = prices[i] - minimum
        return maximum
                

            
            

        