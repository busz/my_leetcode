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
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        vector<vector<int>> result;
        if(root == NULL)
            return result;
        queue<TreeNode *> nodeQ;
        queue<int> levelQ;
        nodeQ.push(root);
        levelQ.push(1);
        int pre = 1;
        vector<int> levelVec;
        while(nodeQ.size())
        {
            TreeNode *node = nodeQ.front();
            int level = levelQ.front();
            nodeQ.pop();
            levelQ.pop();
            if(node->left != NULL)
            {
                nodeQ.push(node->left);
                levelQ.push(level+1);
            }
            if(node->right != NULL)
            {
                nodeQ.push(node->right);
                levelQ.push(level+1);
            }
            if(level == pre)
            {
                levelVec.push_back(node->val);
            }
            else
            {
                pre = level;
                result.push_back(levelVec);
                levelVec.clear();
                levelVec.push_back(node->val);
            }
        }
        result.push_back(levelVec);
        reverse(result.begin(),result.end());
        return result;
    }
};
