'''
Created on 2014-3-27


Leetcoder : add two number:

Problem: 

You are given two linked lists representing two non-negative numbers. The digits
 are stored in reverse order and each of their nodes contain a single digit. Add
  the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8


@author: xqk
'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        r = l1;
        while l1!= None and l2!=None:
            l1.val = l1.val + l2.val
            if l1.val >= 10:
                l1.val = l1.val%10
                if l1.next !=None:
                    
                    l1.next.val = l1.next.val + 1;
                else:
                    l1.next = ListNode(1);
            preL1 = l1
            l1 = l1.next
            
            l2 = l2.next
            
        if l1 == None and l2 != None:
            preL1.next = l2
        if l2 == None:
            while l1 != None:
                if l1.val>=10:
                    l1.val = l1.val%10
                    if l1.next !=None:
                    
                        l1.next.val = l1.next.val + 1;
                    else:
                        l1.next = ListNode(1);
                    l1 = l1.next
                else:
                    break
                    
        return r
        
l1 = ListNode(9)    
l1.next = ListNode(9)
#l1.next.next = ListNode(3)
l2 = ListNode(9)
#l2.next = ListNode(6)
#l2.next.next = ListNode(4)
test =Solution()
r = test.addTwoNumbers(l1, l2)
while r.next!=None:
    print r.val
    r = r.next
print r.val
        