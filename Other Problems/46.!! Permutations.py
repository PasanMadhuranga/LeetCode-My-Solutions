class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.DFS(nums, [], result)
        return result

    def DFS(self, curNums, path, res):
        if (not curNums):
            res.append(path)
            return
        
        n = len(curNums)

        for i in range(n):
            self.DFS(curNums[:i] + curNums[i+1:], path+[curNums[i]], res)
        


# Another solution found in the discussion section
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        p=permutations(nums, n)
        return p
        