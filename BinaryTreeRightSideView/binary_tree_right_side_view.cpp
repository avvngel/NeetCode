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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res {};

        deque<TreeNode*> q {};
        if ( root ) q.push_back( root );

        while ( !q.empty() ){
            TreeNode* rightmost;
            size_t len {q.size()};

            for ( size_t i {0}; i != len; i++ ){
                TreeNode* node {q.front()};
                q.pop_front();
                rightmost = node;
                if ( node->left ) q.push_back(node->left);
                if ( node->right ) q.push_back(node->right);
            }
            res.push_back( rightmost->val );
        }
        return res;
    }
};

