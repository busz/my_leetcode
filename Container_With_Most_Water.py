'''
Created on 2014-7-29

Leetcode : Container_With_Most_Water

Given n non-negative integers a1, a2, ..., an, where each represents a point at
 coordinate (i, ai). n vertical lines are drawn such that the two endpoints of 
 line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
 forms a container, such that the container contains the most water.

Note: You may not slant the container.

@author: xqk
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        if len(height) < 2:
            return 0
        left = 0
        right = len(height) - 1
        max = 0
        
        while left < right:
            cheight = height[left] if height[left] < height[right] else height[right]
            cmax = (right - left  )*cheight
            max = max if max > cmax else cmax
            
            if height[left] < height[right]:
                left = left + 1;
            else:
                right = right - 1;
        return max
                        
test = Solution();
height = [6,2,3,4,5]
print test.maxArea(height)
