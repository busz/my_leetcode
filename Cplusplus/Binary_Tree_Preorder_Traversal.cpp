/*
Leetcode : Binary_Tree_Preorder_Traversal.cpp

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
*/

#include <iostream>
#include <stack>
#include <vector>
using namespace std;


//Definition for binary tree
struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        if(root == NULL)
            return result;
        stack<TreeNode* > nodeStack;
        nodeStack.push(root);
        while(nodeStack.size())
        {
            TreeNode* node = nodeStack.top();
            nodeStack.pop();
            result.push_back(node->val);
            if(node->right != NULL)
                nodeStack.push(node->right);
            if(node->left != NULL)
                nodeStack.push(node->left);

        }
    }
};

int main()
{
    Solution test = Solution();
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    vector<int> result = test.preorderTraversal(root);
    for(int i = 0 ; i < result.size() ; i++)
        cout<<result[i]<<" ";
}

