'''
Created on 2014.7.30

Given a sorted array of integers, find the starting and ending 
position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        r = [-1 ,-1]
        if len(A) == 0:
            return r
        left = 0
        right = len(A) - 1
        
        while left <= right:
            mid = (left + right) /2
            if A[mid] == target:
                break
            else:
                if A[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
         
        if left <= right:
            if mid - 1 < 0 or A[mid - 1] != target:
                r[0] = mid
            else:
                r[0] = self.findLeft(A , left , mid-1 , target)
            if mid + 1 >= len(A) or A[mid+1]!=target:
                r[1] = mid
            else:
               
                r[1] = self.findRight(A,mid+1 , right , target)
        return r
    
    def findLeft(self , A, left , right , target):
        pos = left
        while left <= right:
            mid = (left + right)/2
            if A[mid] < target:
                left = mid + 1
            else:
                if mid - 1 < left or A[mid-1] != target:
                    pos = mid
                    break
                else:
                    right = mid - 1
        return pos
    def findRight(self , A, left , right , target):
        pos = right
        while left <= right:
            mid = (left + right)/2
            if A[mid] > target:
                right = mid - 1
            else:
                if mid + 1 > right or A[mid+1] != target:
                    pos = mid
                    break
                else:
                    left = mid + 1
        return pos
test = Solution()
A = [0,0,0,0,1,2,3,3,4,5,6,6,7,8,8,8,9,9,10,10,11,11]
target = 0
print test.searchRange(A, target)
             
      
        
        
