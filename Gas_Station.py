'''
Created on 2014-8-20

Leetcode : Gas_Station

There are N gas stations along a circular route, where the amount of gas at

 station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to 

travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the 

circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.

'''
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        
        diff = [gas[i] - cost[i] for i in range(len(cost))]
        need = [0 for i in range(len(cost) )]
        remainders = [0 for i in range(len(cost) )]
        rightNeed = 0
        rightRemainder = 0
        for i in range(len(cost) - 1  , -1 , -1):
            
            rightNeed = max(0, rightNeed - diff[i])
            if i>0:
                need[i-1] = rightNeed
            rightRemainder = rightRemainder + diff[i]
            remainders[i] = rightRemainder
   
        start = -1
        leftNeed = 0
        leftRemainder = 0

        index = 0
        while index < len(cost) :   
            if diff[index] >= need[index] and remainders[index] >= leftNeed:
                start = index
                break
    
            leftRemainder = leftRemainder + gas[index] - cost[index]
            if leftRemainder < 0 and abs(leftRemainder) > leftNeed  :
                leftNeed = abs(leftRemainder) 
            index += 1
                
        return start 
    
    
test = Solution()
gas = [1,2,3,3]
cost = [2,1,5,1]
print test.canCompleteCircuit(gas, cost)
                
                
                
