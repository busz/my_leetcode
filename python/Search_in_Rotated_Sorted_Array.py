'''
Created on 2014.7.28

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return 
its index, otherwise return -1.

You may assume no duplicate exists in the array.

'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 0:
            return -1;
        if len(A) == 1:
            if A[0] == target : 
                return 0;
            else:
                return -1
        left = 0;
        right = len(A) - 1;
        while left >= 0 and left <len(A) and right < len(A) and right >= 0 and left < right :
            mid = (left + right)/2;
           
            if A[mid] < target:
                if target <= A[-1]:
                    left = mid + 1
                elif target >= A[0]:
                    if A[mid] >= A[0]:
                        left = mid + 1;
                    else:
                        right = mid - 1;
                else:
                    return -1
                
            elif A[mid] > target:
                if A[0] > target:
                    if A[mid] > A[-1]:
                        left = mid + 1
                    else:
                        right = mid-1;
                    
                elif A[0] < target:
                    
                    right = mid - 1;
                else:
                    return 0
            else:
                return mid;
        
        if left >= 0 and A[left] == target:
            return left
        else:
            return -1 
        
test = Solution()
A = [3,4,5,1,2]
target = 4
print test.search(A, target)
