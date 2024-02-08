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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        return consMaxBTreeRecursive(nums, 0, nums.size());
    }

    TreeNode* consMaxBTreeRecursive(vector<int>& nums, int start, int end) {
        if (start >= end) return NULL;

        int maxNum = nums[start];
        int maxNumI = start;
        for (int i = start + 1; i < end; i++){
            if (nums[i] > maxNum) {
                maxNum = nums[i];
                maxNumI = i;
            }
        }
        TreeNode* root = new TreeNode(maxNum);
        root->left = consMaxBTreeRecursive(nums, start, maxNumI);
        root->right = consMaxBTreeRecursive(nums, maxNumI+1, end);
        return root;
    }
};


// Another Solution Found in the discussion section
// The key idea is:
// 1. We scan numbers from left to right, build the tree one node by one step;
// 2. We use a stack to keep some (not all) tree nodes and ensure a decreasing order;
// 3. For each number, we keep pop the stack until empty or a bigger number; 
//    The bigger number (if exist, it will be still in stack) is current number's root, 
//    and the last popped number (if exist) is current number's left child (temporarily, 
//    this relationship may change in the future); Then we push current number into the stack.


class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        vector<TreeNode*> stk;
        for (int i = 0; i < nums.size(); ++i)
        {
            TreeNode* cur = new TreeNode(nums[i]);
            while (!stk.empty() && stk.back()->val < nums[i])
            {
                cur->left = stk.back();
                stk.pop_back();
            }
            if (!stk.empty())
                stk.back()->right = cur;
            stk.push_back(cur);
        }
        return stk.front();
    }
};