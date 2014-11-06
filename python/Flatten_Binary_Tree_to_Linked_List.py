'''
Created on 2014-7-29

Leetcode : Flatten Binary Tree to Linked List 

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points 
to the next node of a pre-order traversal.


'''

# Definition for a  binary tree node

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None:
            return
        last , root = self.rightTree(root);
        
    def rightTree(self,root):
        last = None
        if root.left == None and root.right == None:
            last = root
        elif root.left == None and root.right != None:
            last , root.right = self.rightTree(root.right)
        elif root.left != None and root.right == None:
            last ,root.right = self.rightTree(root.left)
            root.left = None
        else:
            rightNode = root.right
            last ,root.right = self.rightTree(root.left)
            root.left = None
            
            nlast ,last.right = self.rightTree(rightNode);
            last = nlast
        return last ,root;
            
test = Solution()
tree = []
for i in range(6):
    tree.append(TreeNode(i+1));
tree[0].left = tree[1]
tree[1].left = tree[2]
tree[1].right = tree[3]
tree[0].right = tree[4]
tree[4].right = tree[5]

test.flatten(tree[0])
node = tree[0]
while node!= None:
    print node.val
    node = node.right
            
        
