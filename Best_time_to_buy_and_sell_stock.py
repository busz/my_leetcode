'''
Created on 2014-3-19


leetcoder : best time to buy and sell stock

Problem : Say you have an array for which the ith element is the price of a 
given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and
 sell one share of the stock), design an algorithm to find the maximum profit.


@author: xqk
'''


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0;
        if len(prices) == 2 and prices[0]> prices[1]:
            return 0;
        maxprofit = 0;
        minprice = prices[0]
        for i in range(len(prices) - 1):
            if prices[i+1] < minprice:
                minprice = prices[ i + 1];
            else :
                profit = prices[i+1] - minprice;
                if profit > maxprofit:
                    maxprofit = profit
        return maxprofit
        
        
prices = [2, 5, 3, 8, 9, 4];
test = Solution();
print test.maxProfit(prices);