'''
Created on 2014-8-7

Leetcode : Edit_Distance

Given two words word1 and word2, find the minimum number of steps required to

 convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

'''

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        arr = [ [0 for i in range(len(word1)+1)] for i in range(len(word2)+1) ]
        
        for i in range(len(word1) + 1):
            arr[0][i] = i
        for i in range(len(word2)+1):
            arr[i][0] = i
        for x in range(1,len(word2)+1):
            for y in range(1,len(word1)+1):
                if word1[y-1] == word2[x-1]:
                    dis = 0
                else:
                    dis = 1
                arr[x][y] = min(arr[x-1][y]+1 , arr[x][y-1]+1 , arr[x-1][y-1]+dis) 
        return arr[len(word2)][len(word1)]

test = Solution()
word1 = 'sailn'
word2 =  'failing'
print test.minDistance(word1, word2)
