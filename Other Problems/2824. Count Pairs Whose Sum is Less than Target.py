class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        n = len(nums)
        for i in range(n):
            upBound = target - nums[i]
            for j in range(i):
                if (nums[j] >= upBound or i == j):
                    continue
                pairs += 1
        return pairs
            

# Another solution found in the discussion section
# Approach
# The Two-Pointers Approach is a common technique to solve problems involving arrays or sequences. In this case, you can use two pointers, often referred to as the "left" and "right" pointers, to traverse the array and find pairs that satisfy the given condition.

# Here's a high-level overview of the approach:

# 1.) Sort the array in ascending order. Sorting helps in efficiently exploring pairs with sums less than the target value.

# 2.) Initialize two pointers, left and right, pointing to the first and last elements of the sorted array, respectively.

# 3.) Initialize a variable count to keep track of the count of valid pairs.
# While the left pointer is less than the right pointer:
# If the sum of the elements at left and right is less than the target value, it means all pairs with the current left element will also satisfy the condition. So, increment the count by right - left and move the left pointer to the right.
# If the sum is greater than or equal to the target, move the right pointer to the left.

# 4.) Continue this process until the left pointer crosses the right pointer.

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        pairs = 0
        while (left < right):
            if (nums[left] + nums[right] < target):
                pairs += right - left
                left += 1
            else:
                right -= 1

        return pairs