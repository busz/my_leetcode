'''
Created on 2014-8-18

Leetcode : 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that

 a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        dict = {}
        for i in range(len(num)):
            for j in range(i+1 , len(num)):
                if dict.has_key(num[i]+num[j]):
                    dict[num[i]+num[j]].append([i,j,num[i] , num[j]])
                else:
                    dict[num[i]+num[j]] = [ [i,j, num[i] , num[j] ] ]
        
        r = []
       
        keys = dict.keys()
        keys.sort()
        for key in keys:
            if target - key >= key:
                if dict.has_key(target - key):
                    for i in range(len(dict[key])):
                        for j in range(len(dict[target - key])):
                            index = dict[key][i][:2] + dict[target - key][j][:2]
                            #print index , len(set(index))
                            if len(set(index)) == 4:
                                newCom = dict[key][i][2:] + dict[target - key][j][2:]
                                newCom.sort()
                                if newCom not in r:
                                    r.append(newCom)
                
        return r
            
        
        
        
        
        
        

test = Solution()
num = [1 ,0, -1, 0 ,-2 ,2]
target = 0
#num = [-491,-468,-450,-415,-414,-374,-357,-333,-305,-292,-274,-272,-271,-258,-241,-240,-227,-217,-196,-184,-161,-120,-116,-110,-110,-98,-92,-47,-27,-10,-8,-7,-4,-1,19,30,53,62,64,65,137,138,145,160,178,179,209,221,243,270,279,283,290,291,305,308,322,345,354,357,365,366,368,371,376,381,381,394,400,406,429,433,445,446,449,470,471,472]
#target = 2873
print test.fourSum(num, target)
