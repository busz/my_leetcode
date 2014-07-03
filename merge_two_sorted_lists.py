'''
Created on 2014-2-27

leetcode : merge two sorted lists

Problem :

Merge two sorted linked lists and return it 
as a new list. The new list should be made 
by splicing together the nodes of the first 
two lists.

Solve :


@author: xqk
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None :
            return l1
       
       
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
           
            
        else:
            head = ListNode(l2.val)
            l2 = l2.next
            
        pos = head
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                node = ListNode(l1.val)
                pos.next = node
                pos = pos.next
                l1 = l1.next
            
            else:
                node = ListNode(l2.val)
                pos.next = node
                pos = pos.next
                l2 = l2.next
            
        if l1 == None:
            pos.next = l2
        else:
            pos.next = l1
        return head

l1 = ListNode(0)
pos = l1
for i in range(5):
    node = ListNode(i+1)
    pos.next = node
    pos = pos.next
pos = l1

l2 = ListNode(1)
pos = l2
for i in range(5):
    node = ListNode( (i+1)*2)
    pos.next = node
    pos = pos.next
pos = l2
while pos !=None:
    print pos.val
    pos = pos.next
test = Solution()
r = test.mergeTwoLists(l1, l2)
while r != None:
    print r.val
    r = r.next