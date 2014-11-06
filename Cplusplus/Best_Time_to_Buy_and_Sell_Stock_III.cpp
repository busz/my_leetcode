/*
Leetcode ; Best_Time_to_Buy_and_Sell_Stock_III.cpp

Say you have an array for which the ith element is the 

price of a given stock on day i.

Design an algorithm to find the maximum profit. You may 

complete at most two transactions.

Note:
You may not engage in multiple transactions at the same 

time (ie, you must sell the stock before you buy again).
*/

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if (prices.size() < 2)
            return 0;
        vector<int> leftPros(prices.size() , 0);
        vector<int> rightPros(prices.size() , 0);
        int minV = prices[0];
        for(int i = 1 ; i < prices.size() ; i++)
        {
            if(prices[i-1] < minV)
                minV = prices[i-1];
            if(prices[i] - minV > leftPros[i-1])
                leftPros[i] = prices[i] - minV;
            else
                leftPros[i] = leftPros[i-1];
                
        }
        int maxV = prices[prices.size() - 1];
        for(int i = prices.size() - 2 ; i >= 0 ; i--)
        {
            if(prices[i+1] > maxV)
                maxV = prices[i+1];
            if(maxV - prices[i] > rightPros[i+1])
                rightPros[i] = maxV - prices[i];
            else
                rightPros[i] = rightPros[i+1];
        }
        int maxP = 0;
        for(int i = 0 ; i < prices.size() ; i++ )
        {
            if(leftPros[i] + rightPros[i] > maxP)
                maxP = leftPros[i] + rightPros[i];
        }
        return maxP; 
    }
};
