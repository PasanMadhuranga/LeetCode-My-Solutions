class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for n in nums:
            if (closest <= 0 and n <= 0 and n > closest):
                closest = n
            elif (closest >= 0 and n >= 0 and n < closest):
                closest = n
            elif (closest <= 0 and n >= 0 and n <= -closest):
                closest = n
            elif (closest >= 0 and n <= 0 and -n < closest):
                closest = n
        return closest

        