'''
Created on 2014-2-26

leetcode : Remove Duplicates from Sorted List

Problem : 
Given a sorted linked list , detect all duplicates 
such that each element appear only once

Solve :  

@author: xqk
'''

#Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None :
            return head
        node = head
        while node.next != None:
            if node.val == node.next.val:
                if node.next.next != None:
                    node.next = node.next.next
                else:
                    node.next = None
                    break
            else:
                node = node.next
        return head
    
head = ListNode(1)
n2 = ListNode(1)
head.next = n2
n3 = ListNode(2)
n2.next = n3
n4 = ListNode(3)
n3.next = n4
n5 = ListNode(3)
n4.next = n5
test = Solution()
l = test.deleteDuplicates(head)
while l != None:
    print l.val
    l = l.next 