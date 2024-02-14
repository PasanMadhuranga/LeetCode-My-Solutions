class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        subLen = len(l)
        ans = [True] * subLen
        for i in range(subLen):
            sortedArr = sorted(nums[l[i]: r[i] + 1])
            diff = sortedArr[1] - sortedArr[0]
            for j in range(1, r[i]-l[i]):
                if ((sortedArr[j+1] - sortedArr[j]) != diff):
                    ans[i] = False
        return ans