'''
Created on 2014-3-19


leetcoder : best to buy and sell stock III

Problem : Say you have an array for which the ith element is the price of a 
given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two 
transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell 
the stock before you buy again).

@author: xqk
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profits = [];
        profit = 0;
        flag = False
        for i in range( len(prices) -1):
            if prices[i+1] - prices[i]>0:
                profit = profit + prices[i+1] - prices[i];
            else:
                profits.append(profit)
                profit = 0;
        maxprofit = max(profits)
        profits.remove(maxprofit)
        maxprofit = maxprofit + max(profits)
        return maxprofit
        
        
prices = [2, 5, 3, 8, 9, 4];
test = Solution();
print test.maxProfit(prices);