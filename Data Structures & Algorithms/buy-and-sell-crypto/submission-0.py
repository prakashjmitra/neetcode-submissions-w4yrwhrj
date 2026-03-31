class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0 
        for i in range(0, len(prices)-1, 1):
            print(len(prices[i+1:len(prices)]))
            #print(max(prices[i+1:len(prices)-1]))
            maximum = max(max(prices[i+1:len(prices)]) - prices[i],maximum)
        return maximum
        