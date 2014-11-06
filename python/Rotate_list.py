'''
Created on 2014-3-21

Leetcode : Rotate List

Problem : 

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.


@author: xqk
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None:
            return None
        if k == 0:
            return head
        first = head
        last = head
        result = None
        flag = False
        num = 0;
        for i in range(k):
            if first.next != None :
                first = first.next
                
            else:
                first = head
                
       
       
        while first.next != None:
            last = last.next
            first = first.next
        first.next = head
        result = last.next
        last.next = None
   
            
        
        
            
        return result
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

test = Solution()
r = test.rotateRight(n1, 6)
while r.next != None:
    print r.val
    r = r.next
print r.val
