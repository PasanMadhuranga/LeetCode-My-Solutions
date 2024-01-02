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
