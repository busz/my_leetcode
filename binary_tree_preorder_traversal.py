'''
Created on 2014-2-21

leetcode : Binary Tree Preorder Traversal

Problem : 

Given a binary tree , return the preorder traversal
of its nodes' values

for example :

Given binary tree { 1 , # , 2 , 3}
return [ 1 , 2 , 3 ]

Note : Recursive solution is trivial .
could you do it iteratively?

@author: xqk
'''

#Definition for a ninary tree node

class TreeNode:
    def __init__(self , x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # @param root ,  a tree node
    # @return a list of integers
    def preorderTraversal(self,root):
        r = [];
        if root == None:
            return None
        
        #r.append(1);
       
        r  = self.travel(root, r);
        return r;
        
    def travel(self , root , r):
        if root == None:
            return r
        else:
            r1 = r.append(root.val);
        r1 = self.travel(root.left , r)
        
        r1 = self.travel(root.right , r)
        return r1


if __name__=="__main__":
    test = Solution();
    n1 = TreeNode(1);
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n2.right = n3
    r = test.preorderTraversal(n1)
    print r
    

        
