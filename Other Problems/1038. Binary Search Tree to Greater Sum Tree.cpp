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
    // Function to convert BST to a Greater Sum Tree
    TreeNode* bstToGst(TreeNode* root) {
        // Start the conversion with an initial greatParentSum of 0
        return calGst(root, 0);
    }

    // Helper function to calculate the Greater Sum Tree
    TreeNode* calGst(TreeNode* root, int greatParentSum) {
        // Base case: if the current node is NULL, return it
        if (root == NULL){
            return root;
        }
        // Update the value of the current node by adding the sum of all nodes greater than it
        // and the sum passed down from its parent node(s)
        root->val += treeSum(root->right) + greatParentSum;

        // Recursively convert the right subtree, carrying forward the current greatParentSum
        calGst(root->right, greatParentSum);

        // Recursively convert the left subtree
        // The new greatParentSum for the left child is the updated value of the current node
        calGst(root->left, root->val);

        // Return the root of the modified subtree
        return root;
    }

    // Function to compute the sum of all nodes in a tree
    int treeSum(TreeNode* root) {
        // If the node is NULL, return 0; else, return the sum of the value of the node
        // and the sums of its left and right subtrees
        return root ? root->val + treeSum(root->left) + treeSum(root->right) : 0;
    }
};


// Another solution found in the discussion section
class Solution {
public:
    // A variable to keep track of the cumulative sum of nodes visited so far
    int pre = 0;

    // Function to convert BST to a Greater Sum Tree
    TreeNode* bstToGst(TreeNode* root) {
        // If there is a right child, first convert the right subtree
        if (root->right) bstToGst(root->right);

        // Update the value of the current node by adding it to the cumulative sum 'pre'
        // This step accumulates the values of all nodes greater than the current node
        pre = root->val = pre + root->val;

        // If there is a left child, then convert the left subtree
        if (root->left) bstToGst(root->left);

        // Return the root of the modified subtree
        return root;
    }
};
