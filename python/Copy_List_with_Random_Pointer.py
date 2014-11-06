'''
Created on 2014-8-21

Leetcode : Copy_List_with_Random_Pointer

A linked list is given such that each node contains an additional 

random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None
        start = head
        while start:
            node = RandomListNode(start.label)
            node.next = start.next
            start.next = node
            start = node.next
        newHead = head.next
        node = head.next
        start = head
        while start:
            if start.random:
                node.random = start.random.next
            start = node.next
            if node.next:
                node = node.next.next
        start = head
        node = head.next
        while start:
            start.next = start.next.next
            start = start.next
            if node.next:
                node.next = node.next.next
                node = node.next
        return newHead
