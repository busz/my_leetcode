'''
Created on 2014.8.17

Leetcode : Distinct_Subsequences

Given a string S and a string T, count the number of distinct subsequences 

of T in S.

A subsequence of a string is a new string which is formed from the original 

string by deleting some (can be none) of the characters without disturbing 

the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

'''

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
        m = [ [1]+[ 0 for i in range(len(T))] for i in range(len(S)+1) ]
        for y in range(len(T)):
            for x in range(len(S)):
                if S[x] == T[y]:
                    m[x+1][y+1] = m[x][y] + m[x][y+1]
                else:
                    m[x+1][y+1] = m[x][y+1]
        return m[-1][-1] 
            
test = Solution()
S = "rabbbit"
T = "rabbit"
#S = "aaabbaaaabbbaaaaba"
#T =  "abba"
print test.numDistinct(S, T)       
        
