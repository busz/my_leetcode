/*
Leetcode : Convert_Sorted_Array_to_Binary_Search_Tree.cpp
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
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
    TreeNode *sortedArrayToBST(vector<int> &num) {
        if(num.size() == 0)
            return NULL;
        int left = 0;
        int right = num.size() - 1;
        TreeNode *root = buildTree(num , left , right );
        return root;
    }
    TreeNode *buildTree(vector<int> &num , int left , int right )
    {
        int mid = (left + right)/2;
        TreeNode *root = new TreeNode(num[mid]);
        if(left <= mid - 1)
        {
            root->left = buildTree(num , left , mid - 1 );
        }
        if(right >= mid + 1)
        {
            root->right = buildTree(num , mid + 1 , right );
        }
        return root;
    }
};
