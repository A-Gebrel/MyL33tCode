class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # if the list is in descending order, no need to do anything
        # # return 0 because any investment will return a loss.
        # for i in range(len(prices)-1):
        #     if prices[i] >= prices[i+1]:
        #         pass
        #     else:
        #         return 0
        mostProfit = 0
        buy = 0
        sell = 1
        while(sell < len(prices)):
            profit = prices[sell] - prices[buy]
            if(prices[buy] < prices[sell]):
                mostProfit = max(profit, mostProfit)
            else:
                buy = sell
            sell += 1
        return mostProfit
        
            
        