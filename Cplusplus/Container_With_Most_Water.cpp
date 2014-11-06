/*

Leetcode:Container_With_Most_Water.cpp

Given n non-negative integers a1, a2, ..., an, where each 

represents a point at coordinate (i, ai). n vertical lines 

are drawn such that the two endpoints of line i is at (i, ai) 

and (i, 0). Find two lines, which together with x-axis forms 

a container, such that the container contains the most water.

Note: You may not slant the container.
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        int left = 0;
        int right = height.size() - 1;
        int maxV = 0;
        while(left < right)
        {
            int nHeight = height[left] < height[right]?height[left]:height[right];
            int newCon = nHeight*(right - left);
            if(newCon > maxV)
                maxV = newCon;
            if(height[left]<height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        return maxV;
    }
};

int main()
{
    
}
