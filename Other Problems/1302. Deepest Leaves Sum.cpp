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
    int deepestLeavesSum(TreeNode* root) {
        return DeepestSum(root, 1, findMaxDepth(root));
    }

    int findMaxDepth(TreeNode* root){
        return root ? 1 + max(findMaxDepth(root->left), findMaxDepth(root->right)) : 0;
    }

    int DeepestSum(TreeNode* root,int curDepth, int MaxDepth){
        if (root == NULL){
            return 0;
        }

        if (curDepth == MaxDepth){
            return root->val;
        }

        return DeepestSum(root->left, curDepth+1, MaxDepth) + DeepestSum(root->right, curDepth+1, MaxDepth);
    }
};


// Another Solution found in the discussion section
class Solution {
public:
        int deepestLeavesSum(TreeNode* root) {
        int res = 0, i;
        queue<TreeNode*> q;
        q.push(root);
        while (q.size()) {
            for (i = q.size() - 1, res = 0; i >= 0; --i) {
                TreeNode* node = q.front(); q.pop();
                res += node->val;
                if (node->right) q.push(node->right);
                if (node->left)  q.push(node->left);
            }
        }
        return res;
    }
};