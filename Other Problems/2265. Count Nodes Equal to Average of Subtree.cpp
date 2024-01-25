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
    int averageOfSubtree(TreeNode* root) {
        return countEqualNodes(root);
    }

    int countEqualNodes(TreeNode* root){
        if (root == NULL){
            return 0;
        }

        if (sumNodes(root) / countNodes(root) == root->val){
            return 1 + countEqualNodes(root->left) + countEqualNodes(root->right);
        }
        return countEqualNodes(root->left) + countEqualNodes(root->right);
    }

    int sumNodes(TreeNode* root){
        if (root == NULL){
            return 0;
        }
        return root->val + sumNodes(root->left) + sumNodes(root->right); 
    }

    int countNodes(TreeNode* root){
        if (root == NULL){
            return 0;
        }
        return 1 + countNodes(root->left) + countNodes(root->right); 
    }
};


// Found another solution in the discussion section
class Solution {
public:
    int cnt(TreeNode* root){
        return !root ? 0 : 1 + cnt(root->left) + cnt(root->right);
    }
    int sum(TreeNode* root){
        return !root ? 0 : root->val + sum(root->left) + sum(root->right);
    }
    int averageOfSubtree(TreeNode* root) {
        if(!root)   return 0;
        int ans = averageOfSubtree(root->left) + averageOfSubtree(root->right);
        return sum(root) / cnt(root)==root->val ? ans + 1 : ans;
    }
};