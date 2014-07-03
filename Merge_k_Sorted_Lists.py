'''
Created on 2014-3-25



Leetcoder : Merge k sorted lists


Problem : 

Merge k sorted linked lists and return it as one sorted list. Analyze and 
describe its complexity.


@author: xqk
'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        A = []
        for node in lists:
            while node != None:
                A.append(node.val)
                node = node.next
        sorted(A)
        
        
        
        
        
        
A = None

B = ListNode(1)
#B.next = ListNode(4)
lists = []
lists.append(A)
lists.append(B)

test = Solution()
r = test.mergeKLists(lists)
while r.next != None:
    print r.val
    r = r.next
print r.val