'''
Created on 2014-8-7

Leetcode : Palindrome_Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
  
'''

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        r = []
        if len(s) == 0:
            return r
        if len(s) == 1:
            return [ [s] ]
        length = len(s)
        pos = 0
        while pos < length:
           
            if self.checkPalindrome(s[0 :pos + 1]):
                first =  [s[0:pos+1] ]
                partR = self.partition(s[pos+1:])
             
                if len(partR) != 0 :
                    for item in partR:
                        r.append(first + item)
                if pos + 1 == length:
                    r.append(first)
            pos += 1
        return r
  
    def checkPalindrome(self , s):
        left = 0
        right = len(s) - 1
        flag = True
        while left < right:
            if s[left] != s[right]:
                flag = False
                break
            left += 1
            right -= 1
        return flag

test = Solution()
s = 'aa'
print test.partition(s)

                
        
        
        
        
        
      
