'''
Created on 2014-2-26


leetcode : Remove nth node from end of list

Problem:

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

Solve : 


@author: xqk
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        
        #using double pointers
        
        if head.next == None and n==1:
            return None
        
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        while fast != None:
            fast = fast.next
            slow = slow.next
        if n == 1:
            slow.next = None
        else:
            slow.next = slow.next.next
        
        return head
            
        
        
        #using a stack
        
        #=======================================================================
        # if head.next == None and n==1:
        #     return None
        # node = head
        # q = []
        # while node != None:
        #     if len(q) == n + 1:
        #         q = q[1:]
        #     q.append(node)
        #     node = node.next
        # if len(q) == n:
        #     head = head.next
        # else:
        #     q[0].next = q[1].next
        # return head  
        #=======================================================================
 
n = 2       
head = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h5 = ListNode(5)
head.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
test = Solution()
r = test.removeNthFromEnd(head, n)
while head != None:
    print head.val
    head = head.next

