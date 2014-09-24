/*
Leetcode : Balanced_Binary_Tree.cpp

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a

binary tree in which the depth of the two subtrees of every node never differ by more than 1.
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
    bool isBalanced(TreeNode *root) {
        vector<int> depth(2,0);
        return postOrder(root , depth);
    }


    bool postOrder(TreeNode *root , vector<int> &depth)
    {
        if(root == NULL)
        {
            return true;
        }
        vector<int> leftDepth(2,0);
        vector<int> rightDepth(2,0);
        bool lFlag = postOrder(root->left , leftDepth);
        bool rFlag = postOrder(root->right , rightDepth);
        if(lFlag && rFlag)
        {
            depth[0] = max(leftDepth[0] , leftDepth[1]) + 1;
            depth[1] = max(rightDepth[0] , rightDepth[1]) + 1;
            if(abs(depth[0] - depth[1]) < 2)
                return true;
            else
                return false;
        }
        else
            return false;
    }
};
