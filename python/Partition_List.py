'''
Created on 2014-8-4

Leetcode : Partition_List

Given a linked list and a value x, partition it such that all nodes less 
than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the 

two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

'''
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head== None:
            return None
        leftHead = None
        leftEnd = None
        rightHead = None
        rightEnd = None
        while head != None:
            if head.val < x:
                if leftHead == None:
                    leftHead = head
                    leftEnd = head
                else:
                    leftEnd.next = head
                    leftEnd = leftEnd.next
            else:
                if rightHead == None:
                    rightHead = head
                    rightEnd = head
                else:
                    rightEnd.next = head
                    rightEnd = rightEnd.next
            head = head.next
        if rightEnd != None:
            rightEnd.next = None;
        if leftHead != None:
            leftEnd.next = rightHead
            return leftHead
        else:
            return rightHead
        
test = Solution()
head = ListNode(2)
head.next = ListNode(1)
x = 2
root = test.partition(head, x)
while root != None:
    print root.val
    root = root.next
