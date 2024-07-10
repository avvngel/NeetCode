/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        deque<TreeNode*> queue;

        if ( root ) queue.push_back( root );

        while ( !queue.empty() ){
            vector<int> level_vals {};

            for ( int i = 0, len = queue.size(); i != len; i++ ){
                TreeNode* node {queue.front()};
                queue.pop_front();
                level_vals.push_back(node->val);

                if (node->left) queue.push_back(node->left);
                if (node->right) queue.push_back(node->right);
            }
            res.push_back(level_vals);
        }
        return res;
    }
};

