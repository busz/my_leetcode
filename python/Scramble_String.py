'''
Created on 2014-8-21

Leetcode : Scramble_String

Given a string s1, we may represent it as a binary tree by partitioning it to 

two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces 

a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it 

produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.


'''

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        
        s11 = sorted(s1)
        s22 = sorted(s2)
        if s11 != s22:
            return False
        #print s1,s2
        flag = False
        for i in range(len(s1)):
          
            if (s1[:i] == s2[-i:] or self.isScramble(s1[:i], s2[-i:]) )  and ( s1[i:] == s2[:-i] or self.isScramble(s1[i:], s2[:-i]) ):
                flag = True
                break
        if flag:
            return flag
        
        for i in range(1,len(s1)):
            
            flag = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
           
            if flag:
                return flag
        return flag
        
        
test = Solution()
s1 = "cacbcccbcbaccbabbc"
s2 =  "ccbbbcbbbacaaccccc"
#===============================================================================
# s1 = 'abc'
# s2 = 'cba'
#===============================================================================

print test.isScramble(s1, s2)
            
