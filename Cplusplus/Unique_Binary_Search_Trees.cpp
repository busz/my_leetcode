/*
Leetcode : Unique_Binary_Search_Trees.cpp

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
*/


class Solution {
public:
    int numTrees(int n) {
        
        int sum = 1;
        for(int i = 2 ; i <= n ; i++)
        {
            sum =2*(2*i-1)*sum/(i+1);
        }
        
        return sum;
    }
};
