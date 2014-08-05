'''
Created on 2014.8.6

Leetcode  : Reverse_Linked_List_II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.

'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        if m== n:
            return head
        midHead = None
        midEnd = None
        posNode = None
        if m > 1:
            pos = 1
            leftEnd = head
            while pos != m - 1 :
                leftEnd = leftEnd.next
                pos += 1
            posNode = leftEnd.next
            
            pos = pos + 1
          
        else:
            pos = 1
            leftEnd = None
            posNode = head
        while pos <= n:
            if midHead == None:
                midHead = posNode
                midEnd = posNode
                posNode = posNode.next 
                pos += 1
            else:
                tmpNode = posNode.next
                posNode.next = midHead
                midHead = posNode
                posNode = tmpNode
                pos += 1
                
        if leftEnd != None : 
            leftEnd.next = midHead
            midEnd.next = posNode
            return head
        else:
            midEnd.next = posNode
            return midHead
test = Solution()
head = ListNode(1)
posHead = head
for i in range(2,6):
    newNode = ListNode(i)
    posHead.next = newNode
    posHead = posHead.next
root = test.reverseBetween(head, 2, 5)
while root != None:
    print root.val
    root = root.next
  
        
