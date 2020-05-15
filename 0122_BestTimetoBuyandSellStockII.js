/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy, sell, max_prof = 0;
    let mode = false;
    
    for(buy = 0, sell = 0; sell < prices.length - 1 && buy < prices.length - 1;){
        
        // console.log(buy, sell, mode);
        if(mode){
            if(prices[sell] > prices[sell + 1]){
                max_prof += prices[sell] - prices[buy];
                buy = sell + 1;
                
                mode = false;
            }
            else sell++;
        }
        else{
            if(prices[buy] >= prices[buy + 1]){
                buy++;
            }
            else{
                sell = buy + 1;
                mode = true;
            }
        }
    }
    
    if(buy < sell)
        max_prof += prices[sell] - prices[buy];
    return max_prof;
};