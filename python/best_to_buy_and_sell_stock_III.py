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
        if not prices:
            return 0
        profits1 = [0 for i in range(len(prices) )];
        minV = prices[0]
        for i in range(1,len(prices)):
            minV = min(minV,prices[i])
            profits1[i] = max(profits1[i-1],prices[i] - minV)
            
                
        maxV = prices[-1]
        profits2 = [0 for i in range(len(prices) )];
        for i in range(len(prices) - 2 , -1 , -1):
            maxV = max(maxV , prices[i])
            profits2[i] = max(profits2[i+1] , maxV - prices[i] )
            
               
        #print profits1 , profits2
        sum = 0
        for i in range( len(profits1) ):
            sum = sum if sum > profits1[i] + profits2[i] else profits1[i] + profits2[i]
        return sum
                
        
        
        
prices = [2, 5, 3, 8, 9, 4];
prices = [2,1,2,0,1]
test = Solution();
print test.maxProfit(prices);
