class Solution:
    def jump(self, nums: List[int]) -> int:
        # Get the length of the input array.
        l = len(nums)

        # Initialize variables for the current furthest reach, the current end, and the number of jumps.
        curReach, curEnd, jumps = 0, 0, 0

        # Iterate through the array. Note: we don't need to check the last element, as we are already jumping to the end.
        for i in range(l - 1):
            # Update the furthest reach from the current position.
            curReach = max(curReach, i + nums[i])

            # Check if we have reached the end of the current jump.
            if i == curEnd:
                # Increase the jump count as we need to make a jump to proceed.
                jumps += 1

                # Update the end to be the furthest reach from the current position.
                curEnd = curReach

        # Return the minimum number of jumps needed to reach the end.
        return jumps



# Another Solution found in the discussion section
# int jump(vector<int>& nums) {
#     // Initialize a dynamic programming (DP) vector with size equal to 'nums' and fill it with a large number (10001).
#     // This large number acts as a placeholder to indicate that the minimum number of jumps for each position hasn't been computed yet.
#     vector<int> dp(size(nums), 10001);

#     // Start the recursion from the first position (0) and return the result.
#     return solve(nums, dp, 0);
# }

# // A recursive function to find the minimum number of jumps to reach the end of the array.
# int solve(vector<int>& nums, vector<int>& dp, int pos) {
#     // Base case: If the current position is greater than or equal to the last index of the array,
#     // it means no more jumps are required, so return 0.
#     if(pos >= size(nums) - 1) return 0;

#     // If the minimum number of jumps from the current position has already been computed earlier,
#     // directly return the stored value from the DP array. This step avoids redundant computations.
#     if(dp[pos] != 10001) return dp[pos];

#     // Iterate through all possible jumps from the current position based on the value at nums[pos].
#     for(int j = 1; j <= nums[pos]; j++) {
#         // Recursively calculate the number of jumps needed from the new position (pos + j) and add 1 to it
#         // (since making a jump from the current position). Compare this with the current value in dp[pos]
#         // and update dp[pos] with the minimum of these two values.
#         dp[pos] = min(dp[pos], 1 + solve(nums, dp, pos + j));
#     }

#     // Return the minimum number of jumps needed to reach the end from the current position.
#     return dp[pos];
# }



# Another Solution found in the discussion section
# int jump(vector<int>& nums) {
#     // Determine the size of the input array.
#     int n = size(nums);

#     // Initialize a dynamic programming (DP) vector with the size equal to 'nums' and fill it with a large number (10001).
#     // This large number indicates that the minimum number of jumps for each position hasn't been computed yet.
#     vector<int> dp(n, 10001);

#     // Set the last element of the DP array to 0 because no jumps are required if you are already at the end.
#     dp[n - 1] = 0;

#     // Iterate through the array in reverse order, starting from the second-to-last element.
#     for (int i = n - 2; i >= 0; i--) {
#         // For each index, explore all possible jump sizes based on the value at nums[i].
#         for (int jumpLen = 1; jumpLen <= nums[i]; jumpLen++) {
#             // Calculate the minimum number of jumps needed for this index.
#             // We add 1 to represent the jump from the current position and add the number of jumps
#             // needed from the position we would land on after the jump.
#             // The min(n - 1, i + jumpLen) ensures we don't go out of bounds of the array.
#             dp[i] = min(dp[i], 1 + dp[min(n - 1, i + jumpLen)]);
#         }
#     }

#     // After filling the DP array, return the value at the first index, which represents the minimum number
#     // of jumps needed to reach the end from the start of the array.
#     return dp[0];
# }
