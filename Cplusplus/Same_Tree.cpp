/*
Leetcode : Same_Tree.cpp

Given two binary trees, write a function to check if

they are equal or not.

Two binary trees are considered equal if they are

structurally identical and the nodes have the same value.


*/


#include <iostream>


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
    bool isSameTree(TreeNode *p, TreeNode *q) {
        if(p == NULL && q == NULL)
        {
            return true;
        }
        else if ( !(p && q) )
        {
            return false;
        }
        else
        {
            if(p->val == q->val)
            {
                return isSameTree(p->left , q->left) && isSameTree(p->right , q->right);
            }
            else
            {
                return false;
            }
        }
    }
};

int main()
{
    Solution test = Solution();
    TreeNode *root1 = new TreeNode(1);
    TreeNode *node12 = new TreeNode(2);
    TreeNode *node13 = new TreeNode(3);
    node12->right = node13;
    root1->left = node12;

    TreeNode *root2 = new TreeNode(1);
    TreeNode *node22 = new TreeNode(2);
    TreeNode *node23 = new TreeNode(3);
    node22->right = node23;
    root2->left = node22;
    cout<<test.isSameTree(root1 , root2)<<endl;
    return 0;
}
