/*
Leetcode : Path_Sum.cpp

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

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
    bool hasPathSum(TreeNode *root, int sum) {
        if(root == NULL)
            return false;
        queue<TreeNode *> q;
        q.push(root);
        while(q.size())
        {
            TreeNode * node = q.front();
            q.pop();
            if(node->val == sum && node->left == NULL && node->right == NULL)
                return true;
            if(node->left != NULL)
            {
                node->left->val += node->val;
                q.push(node->left);
            }
            if(node->right != NULL)
            {
                node->right->val += node->val;
                q.push(node->right);
            }
        }
        return false;
    }
};
