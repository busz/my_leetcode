/*
Leetcode : Minimum_Depth_of_Binary_Tree.cpp

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path

from the root node down to the nearest leaf node.
*/

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int minDepth(TreeNode *root) {
        int depth = 10000;
        if(root == NULL)
            return 0;
        stack<TreeNode *> nodeStack;
        root->val = 1;
        nodeStack.push(root);
        while(nodeStack.size())
        {
            TreeNode *node = nodeStack.top();
            nodeStack.pop();
            if(node->left == NULL && node->right == NULL)
            {
                if(node->val < depth)
                    depth = node->val;
            }
            if(node->left != NULL)
            {
                node->left->val = node->val + 1;
                nodeStack.push(node->left);
            }
            if(node->right != NULL)
            {
                node->right->val = node->val + 1;
                nodeStack.push(node->right);
            }
        }
        return depth;

    }
};
