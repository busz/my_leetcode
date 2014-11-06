'''
Created on 2014.8.16

Leetcode : Next_Permutation

Implement next permutation, which rearranges numbers into the lexicographically 

next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible 

order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding 

outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

'''

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        for i in range(len(num) - 1, 0,-1):
            if num[i-1] < num[i]:
                for j in range(len(num) - 1 , i - 1 , -1):
                    if num[j] > num[i-1]:
                        num[j] , num[i-1] = num[i-1] , num[j]
                       
                        rightPart = num[i:]
                        rightPart.sort()
                        num = num[:i] + rightPart
                        return num
        num.sort()
        return num
    
test = Solution()
num = [2,3,1]
print test.nextPermutation(num)
