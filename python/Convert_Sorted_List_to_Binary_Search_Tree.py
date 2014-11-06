'''
Created on 2014.8.3

Leetcode : Convert_Sorted_List_to_Binary_Search_Tree

Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.


'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head == None:
            return None;
        num = 0 
        root  = head
        while root != None:
            num = num + 1;
            root = root.next
        return self.sortListToBST(head, 0, num -1  )[1]
        
    def sortListToBST(self , head , start , end):
        
        if start > end:
            return head , None
        
        mid = (start + end)/2
       
        head , left = self.sortListToBST(head, start, mid - 1)
        
        root = TreeNode(head.val)
      
        head = head.next
        
        root.left = left
        head , root.right = self.sortListToBST(head, mid + 1, end)
        
        return head , root
    
test = Solution()
head = ListNode(3)
head.next = ListNode(5)
head.next.next = ListNode(8)
test.sortedListToBST(head)
