class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mostProfit = 0
        left = 0
        right = 1
        while(right < len(prices)):
            profit = prices[right] - prices[left]
            if(prices[left] < prices[right]):
                mostProfit = max(profit, mostProfit)
            else:
                left = right
            right += 1
        return mostProfit
        
            
        