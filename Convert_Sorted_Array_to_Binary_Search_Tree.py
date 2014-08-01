'''
Created on 2014.8.1


Convert_Sorted_Array_to_Binary_Search_Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if num == None or len(num) == 0:
            return None
        if len(num) == 1:
            return TreeNode(num[0]);
        else:
            length = len(num)
            root = TreeNode(num[length/2])
            root.left = self.sortedArrayToBST(num[:length/2])
            root.right = self.sortedArrayToBST(num[length/2+1:])
            return root
            
    
test = Solution()
num = [1,2,3,4,5]
root = test.sortedArrayToBST(num)
queue = [root]
while len(queue)!=0:
    node = queue[0]
    queue = queue[1:]
    print node.val
    if node.left != None:
        queue.append(node.left)
    if node.right != None:
        queue.append(node.right)
