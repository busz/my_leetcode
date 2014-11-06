'''
Created on 2014-8-7

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.


'''
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        
        s = s.lower()
       
        left = 0
        right = len(s) - 1
        while not self.checkChar(s[left]) and left < right:
            left += 1
        
        while not self.checkChar(s[right]) and right > left:
            right -= 1
        
        flag = True
        while left < right:
          
            if s[left] != s[right]:
                flag = False
                break
            left += 1
            right -= 1
            while not self.checkChar(s[left]) and left < right:
                left += 1
           
            while not self.checkChar(s[right]) and left < right:
                right -= 1
        return flag   
            
    def checkChar(self,s):
        ascii = ord(s[0])
        if ( ascii >= 48 and ascii <= 57)  or (ascii >= 97 and ascii <= 122):
            return True
        else:
            return False
        
        
test = Solution()
#s = "A man, a plan, a canal: Panama"
#s = 'race a car'
s = '.,'
print test.isPalindrome(s)
