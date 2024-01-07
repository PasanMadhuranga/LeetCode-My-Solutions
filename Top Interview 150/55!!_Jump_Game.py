class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Get the length of the array
        l = len(nums)

        # If the array contains only one element, we are already at the last index
        if l == 1: return True

        # Initialize the current position (i) and the farthest reach so far (curReach)
        i, curReach = 0, 0

        # Iterate while the current position is within the farthest reach
        while (i <= curReach):
            # Update the farthest reach. The farthest reach is the maximum of 
            # the current farthest reach and the jump from the current position
            curReach = max(i + nums[i], curReach)

            # If the farthest reach is greater or equal to the last index,
            # then it's possible to reach the last index
            if (curReach >= l-1): return True

            # Move to the next position
            i += 1

        # If we exit the loop, it means we cannot reach the last index
        return False


# Another solution found in the discussion section
# class Solution {
# public:
#     bool canJump(vector<int>& nums) {
#         vector<int> dp(nums.size(), -1);
#         return create(nums, 0, dp);
#     }
# private:
#     bool create(vector<int>& nums, int idx, vector<int>& dp) {
#         if(idx == nums.size() -1) return true;
#         if(nums[idx] == 0) return false;
        
#         if(dp[idx] != -1) return dp[idx]; //overlapping subproblems
#         int reach = idx + nums[idx];
#         for(int jump=idx + 1; jump <= reach; jump++) {
#             if(jump < nums.size() && create(nums, jump, dp)) 
#                 return dp[idx] = true; //memoizing for particular index.
#         }
        
#         return dp[idx] = false; //memoizing for particular index.
#     }
# };