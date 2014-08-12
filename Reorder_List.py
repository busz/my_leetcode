'''
Created on 2014-8-12

Leetcode : Reorder_List

Given a singly linked list L: L0 L1 ...-1 Ln,
reorder it to: L0 Ln L1 Ln-1 L2 Ln-2 ...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None:
            return
        n = 0
        start = head
        while start != None:
            n += 1
            start = start.next
        rightPartNum = n/2
        pos = 0
        start = head
        end = None
        while pos < n - rightPartNum:
            start = start.next
            pos += 1
        while start != None:
            temp = start
            start = start.next
            temp.next = end
            end = temp
            
        start = head.next
        node = head
        while end != None:
            newStart = start.next
            newEnd = end.next
            node.next = end
        
            node = node.next
            node.next = start
            
            node = node.next
            start = newStart
            end = newEnd
        node.next = None
        return head

test = Solution()
head = ListNode(1)
node = head
for i in range(2,7):
    node.next = ListNode(i)
    node = node.next
head = test.reorderList(head)
while head != None:
    print head.val
    head = head.next
            
            
