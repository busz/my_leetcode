'''
Created on 2014-3-19

leetcoder : Path sum

Problem:

Given a binary tree and a sum, determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

@author: xqk
'''
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root  == None :
            return False
        stack = [];
        
        stack.append(root);
        visit = [0];
        
        flag = False;
        while len(stack) != 0 :
            num = len(stack);
            if visit[num-1] == 2:
                visit.pop(num-1);
                stack.pop(num-1)
                continue
            node = stack[num-1];
            visit[num-1] = visit[num-1] + 1
            
            if node.left == None and node.right == None:
                if node.val == sum:
                    flag = True;
                    break;
                else:
                    visit[num-1] = 2
                    continue
            if visit[num-1] == 1:
                if node.left != None:
                    node.left.val = node.left.val + node.val
                    stack.append(node.left)
                    visit.append(0);
            if visit[num-1] == 2:
                if node.right != None:
                    node.right.val = node.right.val + node.val
                    stack.append(node.right)
                    visit.append(0);
                    
            
            
            
        return flag
