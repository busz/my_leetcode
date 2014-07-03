'''
Created on 2014-3-27

Leetcoder : Anagrams

Problem : 

Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.


@author: xqk
'''

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        r = []
        for str in strs:
            start = 0
            end = len(str) - 1
            f = True
            while start < end - 1:
                if str[start]!=str[end]:
                    f = False
                    break;
                else:
                    start = start + 1
                    end = end - 1
            if len(str) == 2 and str[0]!= str[1]:
                f = False
            if len(str) < 2:
                f = False
            if f :
                r.append(str)
        return r
strs = [ 'asdsa' , 'ad' , 'asddsa' , '']
test = Solution()
print test.anagrams(strs)