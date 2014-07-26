'''
Created on 2014.7.26

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) <= 1:
            return len(A);
        pos = 1;
        current = A[0];
        num = 1;
        while pos < len(A):
            if A[pos] == current:
                num = num + 1;
                if num >2 :
                    A.pop(pos)
                else:
                    pos = pos + 1;
            else:
                current = A[pos];
                num = 1;
                pos = pos + 1;
        return len(A)
test = Solution();
A = []
#A = [1,1,1,2,2,3]
print test.removeDuplicates(A)
            
            
            
