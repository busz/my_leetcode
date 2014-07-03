'''
Created on 2014-2-25


Leetcode : Populating next right pointers 
in each node II

Problem : 

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.

Solve : 


@author: xqk
'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:
            return root
        q = [root]
        num = 1
        nextNum = 0
        while len(q) != 0:
            node = q[0]
            if node.left != None : 
                q.append(node.left);
                nextNum = nextNum + 1
            if node.right != None:
                q.append(node.right);
                nextNum = nextNum + 1
            
            if num == 1:
                node.next = None
                num = nextNum
                nextNum = 0
            else:
                node.next = q[1]
                num = num -1
            q = q[1:]
            
        return root       
            

root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n7 = TreeNode(7)

n2.left = n4
n2.right = n5
n3.right = n7

root.left = n2
root.right = n3


test = Solution()
r = test.connect(root)

q = [root , n2 , n3, n4 , n5 , n7]
for node in q:
    if node.next != None:
        print node.next.val
    else:
        print 'No next',node.val
