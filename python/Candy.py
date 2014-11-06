
'''
Created on 2014-8-12

Leetcode : candy

There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

'''




class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        arr = [ [ 1 for i in range(len(ratings))] for i in range(2) ]
       
        for i in range(1,len(arr[0])):
            if ratings[i] > ratings[i-1]:
                arr[0][i] = arr[0][i-1]+1
          
        num = len(arr[0]) - 1
      
        for i in range(1,len(arr[0])):
            if ratings[num - i + 1] < ratings[num - i]:
                arr[1][num - i] = arr[1][num - i + 1] + 1
          
        sumV = 0
        for i in range(len(arr[0])):
            sumV += max(arr[0][i] , arr[1][i])
        return sumV
