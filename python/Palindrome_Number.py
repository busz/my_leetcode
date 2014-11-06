'''
Created on 2014-8-4

Leetcode : Palindrome Number 

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction 
of using extra space.

You could also try reversing an integer. However, if you have solved the problem

 "Reverse Integer", you know that the reversed integer might overflow. 
 How would you handle such case?

There is a more generic way of solving this problem.

'''

class Solution:
    # @return a boolean
   
    def isPalindrome(self, x):
        if x < 0:
            return False
        reverseX = self.reverse(x)
        if reverseX ^ x == 0:
            return True
        else:
            return False
    
        
    def reverse(self, x):
        r = 0;
        if x == 0 :
            return 0 
        f = x/abs(x);
        x = x*f
        while(x):
            r = r*10 + x%10
            x = x/10
            
        return r*f
        
        
test = Solution()

x = 1231

print test.isPalindrome(x)
