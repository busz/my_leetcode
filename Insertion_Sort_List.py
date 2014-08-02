'''
Created on 2014-8-2

Leetcode : Insertion_Sort_List

Sort a linked list using insertion sort.

'''

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None or head.next == None:
            return head
        
        root = head
        
        while head.next != None:
            if head.val <= head.next.val:
                head = head.next
                continue
            
            #print head.next.val
            if head.next.val <= root.val:
                
                nextNode = head.next.next
                head.next.next = root
                root = head.next
                head.next = nextNode
                
                
            else:
                pre = root
                while pre.next.val < head.next.val :
                    pre = pre.next
                
                
                       
                nextNode = head.next.next
                insertNode = pre.next
                
                pre.next = head.next
                pre.next.next = insertNode
                
                head.next = nextNode
                
                        
            
            
            if head == None:
                break
            
            
        return root
    
    
test = Solution()
root = ListNode(2)
root.next = ListNode(3)
root.next.next = ListNode(2)


head = root


root = test.insertionSortList(head)
while root != None:
    print root.val
    root = root.next

