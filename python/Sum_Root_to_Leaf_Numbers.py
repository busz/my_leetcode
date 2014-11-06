'''
Created on 2014.7.27

Leetcode : Sum Root to Leaf Numbers

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.


'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root == None:
            return 0
        sum = 0
        
        queue = [root];
        root.val = root.val
        while len(queue) != 0:
            node = queue[0]
            queue.pop(0);
            if node.left == None and node.right == None:
                sum = sum + node.val 
            if node.left != None:
                node.left.val = node.val*10 + node.left.val;
                queue.append(node.left);
                
            if node.right != None:
                node.right.val = node.val*10 + node.right.val;
                queue.append(node.right);
        return sum

test = Solution();
root = TreeNode(3)
node21 = TreeNode(9)
node22 = TreeNode(2)
node31 = TreeNode(1)
node32 = TreeNode(7)
node22.left = node31
node22.right = node32
root.left = node21
root.right = node22
print test.sumNumbers(root)  
