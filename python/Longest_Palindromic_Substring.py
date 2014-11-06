'''
Created on 2014.8.15

Leetcode : Longest_Palindromic_Substring

Given a string S, find the longest palindromic substring in S. You may assume 

that the maximum length of S is 1000, and there exists one unique longest palindromic substring

'''

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if not s:
            return s
        nS = '#'
        for char in s:
            nS += char + "#"
        nS += '#'
        maxRadius = 0
        maxCentor = 0
        rightRange = 2;
        id = 1
        arr = [ 1 for i in range(len(nS)) ]
        
        for i in range(1,len(nS)):
            if rightRange > i:
                arr[i] = min( arr[2*id - i] , rightRange - i)
            else:
                arr[i] = 1
            
            
            while i - arr[i] >= 0 and i + arr[i] < len(nS) and nS[i+arr[i]] == nS[i - arr[i]]:
                arr[i] += 1
            if i+arr[i] > rightRange:
                rightRange = i + arr[i]
                id = i
            if arr[i] > maxRadius:
                maxRadius = arr[i]
                maxCentor = i
        
        result = [ char for char in nS[maxCentor - maxRadius + 1 : maxCentor + maxRadius - 1] if char != '#' ]
        return ''.join(result)
            

test = Solution()
s = 'babdfdac'
print test.longestPalindrome(s)
