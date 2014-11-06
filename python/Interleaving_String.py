'''
Created on 2014.8.9

Interleaving_String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
'''
class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s1) == 0 or len(s2) == 0:
            return s1+s2 == s3
        if len(s1) + len(s2) != len(s3):
            return False
        arr = [ [False for i in range(len(s2)+1)] for i in range(len(s1)+1) ]
        arr[0][0] = True
        for i in range(len(s1)):
            if s1[i] == s3[i]:
                arr[i+1][0] = True
        for i in range(len(s2)):
            if s2[i] == s3[i]:
                arr[0][i+1] = True
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                if arr[i-1][j] == True:
                    if s3[i+j-1] == s1[i-1]:
                        arr[i][j] = True
                        continue
                if arr[i][j-1] == True:
                    if s3[i+j-1] == s2[j-1]:
                        arr[i][j] = True
                        continue
        return arr[len(s1)][len(s2)]    
                 
        
        

test = Solution()
s1='aa'
s2 = 'ab'
s3 = 'abaa'
#===============================================================================
# s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# #s3 = "aadbbcbcac"
# s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
#===============================================================================
print test.isInterleave(s1, s2, s3)
        
            
