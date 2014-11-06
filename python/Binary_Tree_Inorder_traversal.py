'''
Created on 2014-2-21

leetcode : Binary tree Inorder Traversal

Problem:

Given a binary tree , return the inorder traversal 
of its nodes' values

for example:
Given binary tree { 1 , # ,2 , 3 }
return { 1,3,2 }

Note : Recursive solution is trivial . 
could you do it iteratively

@author: xqk
'''


#Definitipn for a binary tree node 

class TreeNode:
    def __init__(self , x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # @param root , a tree node
    # @return a list of integers
    def inorderTraversal(self , root):
        if root  == None:
            return []
        stack = [root]
        a = []
        while len(stack) != 0:
            node  = stack[-1]
           
            if node.left != None :
                newnode = node.left
                node.left = None
                stack.append(newnode)
            else:
                a.append(node.val)
                stack = stack[:-1]
              
                if node.right != None :
                    stack.append(node.right)
        return a

root = TreeNode(1)
right = TreeNode(2)
rightLeft = TreeNode(3)
right.left = rightLeft
root.right = right

test = Solution()
print test.inorderTraversal(root)