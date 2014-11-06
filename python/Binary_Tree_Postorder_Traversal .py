'''
Created on 2014.7.25

Leetcode  : Binary Tree Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        r = []
        if root == None:
            return r;
        stack = [root]
        visit = [0];
        while len(stack) != 0:
            node = stack[-1]
            if visit[-1] == 2:
                r.append(node.val);
                stack = stack[:-1];
                visit = visit[:-1];
                continue
            
                
            visit[-1] = visit[-1] + 1;
            if visit[-1] == 1:
                if node.left != None:
                    stack.append(node.left);
                    visit.append(0)
                    
            if visit[-1] == 2:
                if node.right != None:
                    stack.append(node.right);
                    visit.append(0)
        return r
        
test = Solution()

root = TreeNode(1);
node2 = TreeNode(2)
node3 = TreeNode(3);
node2.left = node3
node2.right = TreeNode(4)
root.right = node2
print test.postorderTraversal(root)
