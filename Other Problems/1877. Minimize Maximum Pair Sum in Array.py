class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maximum = 0
        for i in range(n//2):
            pairSum = nums[i] + nums[n-1-i]
            if (pairSum > maximum):
                maximum = pairSum

        return maximum

# Another solution found in the discussion section
def minPairSum(self, A):
    return max(a + b for a, b in zip(sorted(A), sorted(A)[::-1]))