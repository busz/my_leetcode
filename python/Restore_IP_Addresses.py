'''
Created on 2014-8-12

Leetcode : Restore_IP_Addresses

Given a string containing only digits, restore it by returning all possible 

valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

'''

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        r = []
        length = len(s)
        for l1 in range(1,4):
            if length - l1 < 3 or not self.checkValid(s[:l1]) :
                break
            for l2 in range(1,4):
                if not self.checkValid(s[l1:l1+l2]) or length - l1 - l2 < 2:
                    break
                for l3 in range(1,4):
                    if not self.checkValid(s[l1+l2:l1+l2+l3]) or length - l1 - l2 - l3 < 1:
                        break
                    if self.checkValid(s[l1+l2+l3:]):
                        ip = s[:l1]+'.'+s[l1:l1+l2]+'.'+s[l1+l2:l1+l2+l3]+'.'+s[l1+l2+l3:]
                        r.append(ip)
        return r
                 
    
    def checkValid(self,s):
       
        if int(s) <= 255 and (len(s) == 1 or s[0] != '0' ):
            return True
        else:
            return False
        
test = Solution()
s = "25525511135"
print test.restoreIpAddresses(s)   
