'''
Created on 2014-3-21


Leetcoder :  swap nodes in pairs

Problem : 

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in 
the list, only nodes itself can be changed.


@author: xqk
'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None :
            return head;
        first = head.next
        last = head
        head = first
        last.next = first.next
        first.next = last
        
        first = first.next
        pos = first
        while first.next != None  :
            last = first.next
            if last.next != None:
                first = last.next
                last.next = first.next
                first.next = last
                pos.next = first
                first = first.next
                pos = first
            else:
                break
        return head
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
#n3.next = n4
test = Solution()
r = test.swapPairs(n1)
while r.next != None:
    print r.val
    r = r.next
print r.val
            
        