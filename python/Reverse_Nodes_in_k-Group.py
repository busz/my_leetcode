'''
Created on 2014.8.8

Reverse_Nodes_in_k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        result = None
        
        start = head
        end = None
        n = 1
        flag = True
        while head != None:
            if n < k:
                n += 1
                
                head = head.next
                
            else:
                flag = False
                head = head.next
                if result == None:
                    result , end = self.reverseKNode(start, k) 
                    
                    
                else:
                    start.next , end  = self.reverseKNode(start.next, k)   
                n = 1
                end.next = head
                start = end
        if flag:        
            return start
        else:
            return result
    def reverseKNode(self , head , k):
        end = head
        start = head
        head = head.next
        end.next = None
        n = 1
        while n < k:
            node = head
            head = head.next
            node.next = start
            start = node
            n += 1
        return start , end
            
test = Solution()
head = ListNode(1)
node = head
for i in range(2,6):
    node.next = ListNode(i)
    node = node.next
k = 3
node = test.reverseKGroup(head, k)
while node != None:
    print node.val
    node = node.next
    
