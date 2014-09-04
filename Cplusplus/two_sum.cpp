/*
Leetcode : two_sum.cpp

Given an array of integers, find two numbers such that

they add up to a specific target number.

The function twoSum should return indices of the two

numbers such that they add up to the target, where index1

must be less than index2. Please note that your returned

answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one

solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
*/

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        vector<int> result;
        map<int , int> table;
        map<int , int>::iterator pos;
        for(int i = 0 ; i < numbers.size() ; i++)
        {
            pos = table.find(target - numbers[i]);
            if(pos != table.end())
            {
                result.push_back(pos->second);
                result.push_back(i+1);
                break;
            }
            else
            {
                table[numbers[i]] = i+1;
            }
        }
        return result;
    }
};

int main()
{
    Solution test = Solution();
    vector<int> numbers(3,0);
    numbers[0] = 3;
    numbers[1] = 2;
    numbers[2] = 4;

    int target = 6;
    vector<int> vec = test.twoSum(numbers , target);
    for(int i = 0 ; i < vec.size() ; i++)
    {
        cout<<vec[i]<<" ";
    }
    return 0;
}
