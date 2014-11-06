'''
Created on 2014.7.30

Leetcode : Search_in_Rotated_Sorted_Array_II

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

'''

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        
        #=======================================================================
        #life is short , using python
        # if target in A:
        #     return True
        # else:
        #     return False
        #=======================================================================
        return self.find(A , 0 , len(A) - 1 , target);
    def find(self , A , left , right , target):
        if left > right:
            return False;
        mid = (left + right)/2;
        if A[mid] == target:
            return True;
        if A[left] < A[right]:
            if A[mid] > target:
                right = right - 1
                return self.find(A , left , right , target);
            else:
                left = left + 1;
                return self.find(A , left , right , target);
        else:
            return self.find(A , mid + 1 , right , target) or self.find(A , left , mid - 1, target);
        
        
        
test = Solution()
A = [1,1,3,1]
target = 3

print test.search(A, target)
