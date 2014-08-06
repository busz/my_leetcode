'''
Created on 2014-8-6

Leetcode : Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating 

characters. For example, the longest substring without repeating letters for 
"abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring 
is "b", with the length of 1.



'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0 :
            return 0
        maxLength = 1
        
        bottom = 0
        
        arr = [-1 for i in range(128)]
        
        for i in range(len(s)):
            pos = ord(s[i])
            
            if arr[pos] == -1:
                arr[pos] = i
              
            elif arr[pos] < bottom:
                    arr[pos] = i
                 
            else:
                maxLength = max(maxLength , i  - bottom)
                
                if arr[pos] >= bottom and i - arr[pos]  > maxLength:
                    bottom = arr[pos] + 1
                    maxLength = i - arr[pos] 
                   
                    arr[pos] = i
                else:
                    bottom = arr[pos] + 1
                    arr[pos] = i
                
        maxLength = max(len(s)  - bottom , maxLength)      
           
            
            
        return maxLength
test = Solution()
s='wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'
#s = "qopubjguxhxdipfzwswybgfylqvjzhar"
print test.lengthOfLongestSubstring(s)
            
        
