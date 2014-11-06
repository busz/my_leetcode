'''
Created on 2014.7.27

Leetcode : Longest Common Prefix 

Write a function to find the longest common
 prefix string amongst an array of strings.

'''

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        
        if strs == None or len(strs) == 0 or len(strs[0]) ==0:
            return ''
        pos = 0
        
        
        flag = True
        while pos < len(strs[0]):
            current = strs[0][pos]
            for i in range(len(strs) - 1):
                if pos < len(strs[i+1]) and strs[i+1][pos] == current:
                    pass
                else:
                    flag = False
                    break;
            if not flag:
                
                break;
            pos = pos + 1
            
        return strs[0][:pos]     
    
test = Solution();
strs = [ 'asdsaf' , 'asd' , 'a']
print test.longestCommonPrefix(strs)    
