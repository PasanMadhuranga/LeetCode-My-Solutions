class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if (not nums):
            return []
        ranges = [nums[0]]
        i = 0
        n = len(nums)
        for i in range(1, n):
            if (nums[i-1] + 1 != nums[i]):
                if (ranges[-1] != nums[i-1]):
                    ranges[-1] = str(ranges[-1]) + "->" + str(nums[i-1])
                else:
                    ranges[-1] = str(ranges[-1])
                ranges.append(nums[i])
        if (ranges[-1] != nums[-1]):
            ranges[-1] = str(ranges[-1]) + "->" + str(nums[-1])
        else:
            ranges[-1] = str(ranges[-1])
        return ranges
