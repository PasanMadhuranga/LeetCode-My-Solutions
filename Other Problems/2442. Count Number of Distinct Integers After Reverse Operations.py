class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            numsSet.add(num)
            reversedNum = 0
            while num:
                reversedNum = reversedNum * 10 + num % 10
                num //= 10
            numsSet.add(reversedNum)
        return len(numsSet)
        


# Another solution found in the discussion section
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        fullList = []
        for num in nums:
            fullList.append(int(str(num)[::-1]))
        
        return len(set(fullList + nums))
        