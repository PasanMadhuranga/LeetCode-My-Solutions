from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(count for ele, count in Counter(nums).items() if ele < num) for num in nums]


# Optimized solution
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        occurrences = [0] * 101

        for num in nums:
            occurrences[num] += 1

        for i in range(1, 101):
            occurrences[i] += occurrences[i-1]
        
        ans = []
        for num in nums:
            if (num):
                ans.append(occurrences[num-1])
            else:
                ans.append(0)
        
        return ans