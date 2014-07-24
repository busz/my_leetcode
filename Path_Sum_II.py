'''
Created on 2014.7.24

Leetcode : Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]


'''


# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root  == None :
            return []
        stack = [];
        
        stack.append(root);
        visit = [0];
        
        r = []
        current = [root.val,root.val];
        while len(stack) != 0:
            node = stack[-1];
            #print current
            if visit[-1] == 2:
                stack = stack[:-1]
                visit = visit[:-1];
                current[0] = current[0] - current[-1];
                current = current[:-1];
                continue
            
            if node.left ==None and node.right == None:
                
                if current[0]  == sum:
                    
                    r.append(current[1:]);
                
                stack = stack[:-1]
                visit = visit[:-1];
                current[0] = current[0] - current[-1];
                current = current[:-1];
                continue;
            
            visit[-1] = visit[-1]+1;
                       
            
            if visit[-1] == 1:
                if node.left != None:
                    stack.append(node.left);
                    visit.append(0);
                    current.append(node.left.val);
                    current[0] = current[0] + node.left.val;
            if visit[-1] == 2:
                if node.right != None:
                    stack.append(node.right);
                    visit.append(0);
                    current.append(node.right.val);
                    current[0] = current[0] + node.right.val;
        return r
            
                    
test = Solution();

root = TreeNode(5);
node21 = TreeNode(4)
node22 = TreeNode(8)
node31 = TreeNode(11)
node32 = TreeNode(13)
node33 = TreeNode(4)
node41 = TreeNode(7)
node42 = TreeNode(2)
node43 = TreeNode(1)

node31.left = node41
node31.right = node42

node33.left = TreeNode(5)

node33.right = node43
node21.left = node31
node22.left = node32
node22.right = node33
root.left = node21
root.right = node22

print test.pathSum(root, 22)

            
        
        
        
