/*

leetcode : Binary_Tree_Postorder_Traversal.cpp

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

*/

#include <iostream>
#include <vector>
#include <stack>
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
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> postOrderVec;
        if(root == NULL)
            return postOrderVec;
        
        stack<int> traNumStack;
        stack<TreeNode*> traNodeStack;
        traNodeStack.push(root);
        traNumStack.push(0);
        while(traNodeStack.size())
        {
            TreeNode *node = traNodeStack.top();
            int num = traNumStack.top();
            if(num == 0)
            {
                traNumStack.top() = traNumStack.top() + 1;
                if(node->left != NULL)
                {
                    traNodeStack.push(node->left);
                    traNumStack.push(0);
                }


            }
            else if(num == 1)
            {
                traNumStack.top() = traNumStack.top() + 1;
                if(node->right != NULL)
                {
                    traNodeStack.push(node->right);
                    traNumStack.push(0);
                }

            }
            else if(num == 2)
            {
                traNumStack.pop();
                postOrderVec.push_back(node->val);
                traNodeStack.pop();
            }
        }
        return postOrderVec;
    }
};

int main()
{
    Solution test = Solution();
    TreeNode *root = new TreeNode(1);
    TreeNode *node2 = new TreeNode(2);
    TreeNode *node3 = new TreeNode(3);
    node2->right = node3;
    root->left = node2;
    vector<int> postVec = test.postorderTraversal(root);
    for(int i = 0 ; i < postVec.size() ; i++)
    {
        cout<<postVec[i]<<" ";
    }
    return 0;
}
