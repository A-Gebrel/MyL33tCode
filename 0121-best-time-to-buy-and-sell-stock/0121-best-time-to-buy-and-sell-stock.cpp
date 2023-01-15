class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = 0;
        int sell = 1;
        int mostProfit = 0;
        if(prices.size() <= 1)
            return mostProfit;
        while(sell < prices.size())
        {
            int profit = prices[sell] - prices[buy];
            if(prices[buy] < prices[sell])
            {
                mostProfit = max(profit, mostProfit);
            }
            else
            {
                buy = sell;
            }
            sell += 1;
        }
        return mostProfit;
        
    }
};