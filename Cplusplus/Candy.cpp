/*
Leetcode : Candy.cpp

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
*/
class Solution {
public:
    int candy(vector<int> &ratings) {
        vector<int> candyArr(ratings.size() , 0);
        candyArr[0] = 1;
        int sum = 0;
        for(int i = 1 ; i < ratings.size() ; i++)
        {
            if(ratings[i] > ratings[i-1] )
                candyArr[i] = candyArr[i-1] + 1;
            else
                candyArr[i] = 1;
        }
        for(int i = candyArr.size() - 2 ; i >= 0 ; i--)
        {
            if(ratings[i] > ratings[i+1] && candyArr[i] <= candyArr[i+1])
                candyArr[i] = candyArr[i+1] + 1;
            sum += candyArr[i];
        }
        sum += candyArr[candyArr.size() - 1];
        return sum;
    }
};
