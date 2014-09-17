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
    vector<int> inorderTraversal(TreeNode *root) {
        stack<TreeNode*> nodeStack;
        vector<int> inOrder;
        if(root == NULL)
        {
            return inOrder;
        }
        TreeNode * node = root;
        while(node || nodeStack.size())
        {
            while(node)
            {
                nodeStack.push(node);
                node = node->left;
            }
            node = nodeStack.top();
            nodeStack.pop();
            inOrder.push_back(node->val);
            
            node = node->right;
        }
        return inOrder;
    }
};
