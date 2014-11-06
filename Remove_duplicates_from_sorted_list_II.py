'''
Created on 2014-2-26

leetcode : Remove duplicates from sorted list II

Problem : 

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Solve : 


@author: xqk
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
       
        while head and head.next and head.val == head.next.val:
            node = head
            while node and head.val == node.val:
                node = node.next
            head = node
        if not head:
            return head
        
        node = head.next
        pre = head
        
        while node:
            if node.next != None and node.next.val == node.val:
                node = node.next
               
            else:
                if node is pre.next:
                    pre = node
                    node = node.next
                else:
                    pre.next = node.next
                    node = node.next
        return head
            
        
head = ListNode(1)
n2 = ListNode(1)
head.next = n2
n3 = ListNode(2)
n2.next = n3

#===============================================================================
# n4 = ListNode(3)
# n3.next = n4
# n5 = ListNode(3)
# n4.next = n5
#===============================================================================
test = Solution()
l = test.deleteDuplicates(head)
while l != None:
    print l.val
    l = l.next                 
                
