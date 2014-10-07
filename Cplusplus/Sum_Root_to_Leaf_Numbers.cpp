/*
Leetcode :Sum_Root_to_Leaf_Numbers.cpp
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
    int sumNumbers(TreeNode *root) {
        queue<TreeNode *> nodeQ;
        int sum = 0;
        if(root == NULL)
            return sum;
        nodeQ.push(root);
        while(nodeQ.size())
        {
            TreeNode *node = nodeQ.front();
            nodeQ.pop();
            if(node->left == NULL && node->right == NULL)
                sum += node->val;
            if(node->left != NULL)
            {
                node->left->val += node->val*10;
                nodeQ.push(node->left);
            }
            if(node->right != NULL)
            {
                node->right->val += node->val*10;
                nodeQ.push(node->right);
            }

        }
        return sum;
    }
};
