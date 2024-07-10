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
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
private:
    int dfs(TreeNode* node, int branch_max){
        if ( !node ) return 0;
        
        branch_max = std::max(branch_max, node->val);
        int count {(node->val == branch_max) ? 1 : 0};
        count += dfs(node->left, branch_max);
        count += dfs(node->right, branch_max);
        return count;
    }
};

