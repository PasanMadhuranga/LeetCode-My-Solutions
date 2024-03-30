class Solution:
    def countVowelStrings(self, n: int) -> int:
        if (n == 1): return 5

        nums = [i for i in range(5, 0, -1)]

        while (n > 2):
            preNum = nums[0]
            nums[0] = sum(nums)
            for i in range(1, 5): 
                curNum = nums[i]
                nums[i] = nums[i - 1] - preNum
                preNum = curNum
            n -= 1

        return sum(nums)


# Another solution found in the discussion section
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24