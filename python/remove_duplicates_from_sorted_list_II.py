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
        if head.val == head.next.val and head.next.next == None:
            return None
        key = head.val
        keyNode = head
        flag = False
        node = head
        while node.next != None:
            if key == node.next.val:
                node.next = node.next.next
                flag = True
            elif flag:
                flag = False
                if keyNode == head:
                    head = node.next
                    node = node.next
                    key = node.val
                    keyNode = head
                
                else:
                    keyNode.next = node.next
                    node = node.next
                    val = node.val
            else:
                keyNode = node
                node = node.next
                key = node.val
        if head.next == None and flag:
            return None
        if node.next == None and flag:
            keyNode.next = None
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
                
