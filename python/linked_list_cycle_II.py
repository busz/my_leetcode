'''
Created on 2014-2-26

leetcode : Linked list cycle II

Problem:

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?

Solve:


@author: xqk
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        if head.next == head:
            return head
        fast = head
        slow = head
        f = False
        while fast.next:
            if (slow == fast and f):
                break
            elif(fast.next.next):
                f= True
                fast = fast.next.next
                slow = slow.next
            else:
                return None
        if fast.next == None:
            return None
        else:
            start = head
            while start != slow:
                start = start.next
                slow = slow.next
            return slow
        
        
head = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
head.next = h2
h2.next = h3
h3.next = h4
h4.next = h2

test = Solution()
start = test.detectCycle(head)
if start != None:
    print start.val