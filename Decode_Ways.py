'''
Created on 2014.8.15

Leetcode : Decode_Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        
        if not s :
            return 0
        arr = [ 0 for i in range(len(s)+1)]
        arr[0] = 1
        if s[0] == '0':
            return 0
        else:
            arr[1] = 1
        for i in range(1,len(s)):
            if s[i] == '0':
                if int(s[i-1]) < 3 and s[i-1]!= '0':
                    arr[i+1] = arr[i - 1]
                else:
                    return 0
            else:
                if int(s[i-1:i+1]) < 27 and s[i-1] != '0':
                    arr[i+1] = arr[i] + arr[i-1]
                else:
                    arr[i+1] = arr[i]
            
        return arr[-1]
    
test = Solution()
s = "101"
print test.numDecodings(s)
