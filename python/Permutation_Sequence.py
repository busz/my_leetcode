'''
Created on 2014.8.16

leetcode : Permutation_Sequence

The set [1,2,3,..,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''

class Solution:
    # @return a string
    def getPermutation(self, n, k):
        if n == 1:
            return '1'
        arr = [1]
        for i in range(1,n):
            arr.append(arr[i-1]*i)
        
        charArr = [str(i) for i in range(1 , n + 1 )]
       
        r = ''
        k = k - 1
        for i in range( n - 1  , 1 , -1 ):
            
            r = r + charArr[k/arr[i]]
            del charArr[k/arr[i]]
            k = k%arr[i]
        if k == 0:
            r = r + charArr[0] + charArr[1]
        else:
            r = r + charArr[1] + charArr[0]
        
        return r
    
test = Solution()
n = 3
k = 1
print test.getPermutation(n, k)
            
        
        
