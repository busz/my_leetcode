/*
Leetcode : Maximum_Depth_of_Binary_Tree.cpp

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the

longest path from the root node down to the farthest

leaf node.


*/

#include <iostream>
#include <vector>

using namespace std;

// Definition for binary tree
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    int maxDepth(TreeNode *root) {
        if(root == NULL)
        {
            return 0;
        }
        else
        {
            int left = maxDepth(root->left);
            int right = maxDepth(root->right);
            int maxD = left > right ? left+1:right+1;
            return maxD;
        }
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
    cout<<test.maxDepth(root)<<endl;
    return 0;
}
