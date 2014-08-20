'''
Created on 2014-8-18

Leetcode : Unique_Binary_Search_Trees_II

Given n, generate all structurally unique BST's (binary search trees) that 

store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        if n== 0:
            return [None]
    
        vArr = range(1,n+1)
        return self.generateTree(vArr)
        
    def generateTree(self , vArr):
        treeList = []
        if len(vArr) == 0:
            treeList.append(None)
        elif len(vArr) == 1:
            treeList.append(TreeNode(vArr[0]))
        else:
            
            for index , value in enumerate(vArr):
                
                leftTreeList = self.generateTree(vArr[:index])
                rightTreeList = self.generateTree(vArr[index+1:])
                treeList += [ self.initTree(value , leftTree , rightTree) for leftTree in leftTreeList for rightTree in rightTreeList ]
            
        return treeList
    
    def initTree(self , value , leftTree , rightTree):
        root = TreeNode(value)
        root.left = leftTree
        root.right = rightTree
        #=======================================================================
        # root.left = self.treeClone(leftTree)
        # root.right = self.treeClone(rightTree)
        #=======================================================================
        return root 
