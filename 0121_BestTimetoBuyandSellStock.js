/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let sell, buy, max_prof = 0;
    
    for(buy = 0, sell = 1; sell < prices.length; sell++){
        if(prices[sell] - prices[buy] > max_prof)
            max_prof = prices[sell] - prices[buy];
        
        if(prices[sell] < prices[buy])
            buy = sell;
    }
    
    return max_prof;
};