'''
Created on 2014.7.26

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along
 the shortest path from the root node down to the nearest leaf node.

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
    def minDepth(self, root):
        if root == None:
            return 0
        min = 10000000
        queue = [root];
        root.val = 1;
        while len(queue) != 0:
            node = queue[0]
            queue.pop(0);
            if node.left == None and node.right == None:
                min = node.val if node.val < min else min;
            if node.left != None:
                node.left.val = node.val + 1;
                queue.append(node.left);
                
            if node.right != None:
                node.right.val = node.val + 1;
                queue.append(node.right);
        return min

test = Solution();
root = TreeNode(3)
node21 = TreeNode(9)
node22 = TreeNode(20)
node31 = TreeNode(15)
node32 = TreeNode(7)
node22.left = node31
node22.right = node32
root.left = node21
root.right = node22
print test.minDepth(root)  
