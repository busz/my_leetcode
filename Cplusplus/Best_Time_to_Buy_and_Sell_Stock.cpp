/*
Leetcode : Best_Time_to_Buy_and_Sell_Stock.cpp

Say you have an array for which the ith element is the price

of a given stock on day i.

If you were only permitted to complete at most one transaction

(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
*/

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        if(prices.size() < 2)
            return 0;
        vector<int> cVec(prices.size() , 0);
        int minV = prices[0];
        cVec[0] = prices[0];
        for (int i = 1 ; i < prices.size() ; i++)
        {
            if(prices[i] < minV)
            {
                minV = prices[i];
            }
           cVec[i] = minV;
        }
        vector<int> eVec(prices.size(),0);
        int maxV = prices[prices.size()-1];
        eVec[eVec.size()-1] = prices[prices.size()-1];
        for(int i = prices.size() - 2 ; i >= 0 ; i--)
        {
            if(prices[i] > maxV)
            {
                maxV = prices[i];
               
            }
             eVec[i] = maxV;
        }
        int sum = 0;
        for(int i = 0 ; i < prices.size() - 1 ; i++)
        {
            if(eVec[i+1] - cVec[i] > sum)
                sum = eVec[i+1] - cVec[i];
        }
        return sum;
    }
};
