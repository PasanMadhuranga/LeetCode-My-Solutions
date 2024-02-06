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
    int sumEvenGrandparent(TreeNode* root) {
        if (root == NULL) return 0;
        if (root->val % 2 == 1){
            return  sumEvenGrandparent(root->left) + sumEvenGrandparent(root->right);
        }
        int sum = 0;
        if (root->left != NULL){
            if (root->left->left != NULL) sum += root->left->left->val;
            if (root->left->right != NULL) sum += root->left->right->val;
        }

        if (root->right != NULL){
            if (root->right->left != NULL) sum += root->right->left->val;
            if (root->right->right != NULL) sum += root->right->right->val;
        }

        return sum + sumEvenGrandparent(root->left) + sumEvenGrandparent(root->right);
    }
};


// Another Solution found in the discussion section
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
    int sumEvenGrandparent(TreeNode* root, int p = 1, int gp = 1) {
        return root ? sumEvenGrandparent(root->left, root->val, p)
               + sumEvenGrandparent(root->right, root->val, p)
               + (gp % 2 ? 0 : root->val)  : 0;
    }
};