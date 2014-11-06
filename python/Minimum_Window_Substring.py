'''
Created on 2014-8-22
Leetcode : Minimum_Window_Substring

Given a string S and a string T, find the minimum window in S which will contain

 all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the 

emtpy string "".

If there are multiple such windows, you are guaranteed that there will always 

be only one unique minimum window in S.

'''

class Solution:
    # @return a string
    def minWindow(self, S, T):
        
        if len(S) == 0 and len(T) == 0:
            return ''
        
        start = 0
        left = 0
        right = 0
        win = len(S) + 1
        num = len(T)
        arr = [ [0 for i in range(256)] for i in range(2) ]
        for i in range(len(T)):
            index = ord(T[i])
            arr[0][index] += 1
            arr[1][index] += 1
        
        while right < len(S):
            if arr[0][ord(S[right])] > 0:
                arr[1][ord(S[right])] -= 1
                if arr[1][ord(S[right])] >= 0:
                    num -= 1
                    
            if num == 0:
                while True:
                    if arr[0][ord(S[left])] > 0:
                        if arr[1][ord(S[left])] < 0:
                            arr[1][ord(S[left])] += 1
                        else:
                            break
                    left += 1
                if win > right - left + 1:
                    win = right - left + 1
                    start = left
                    
                    

            right = right + 1
        if win == len(S) + 1:
            return ''
        else:
            return S[start:start+win]

    
test = Solution()
S = "ADOBECODEBANC"
T = 'ABC'
S = 'aa'
T = 'aa'
print test.minWindow(S, T)
            
