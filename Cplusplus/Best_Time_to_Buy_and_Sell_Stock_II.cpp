/*
Leetcode : Best_Time_to_Buy_and_Sell_Stock_II.cpp

Say you have an array for which the ith element 

is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 

You may complete as many transactions as you like 

(ie, buy one and sell one share of the stock multiple times). 

However, you may not engage in multiple transactions at the 

same time (ie, you must sell the stock before you buy again).
*/

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int pros = 0;
        for(int i = 1 ; i < prices.size() ; i++)
        {
            int pro = prices[i] - prices[i-1];
            if (pro > 0)
                pros += pro;
        }
        return pro;
    }
};
