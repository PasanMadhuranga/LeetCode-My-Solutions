class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            if nums == []:
                return [[]]
            x = self.subsets(nums[1:])
            return x + [[nums[0]] + y for y in x]


# Another solution found in the discussion section
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        que=[]
        que.append([])
        for i in nums:
            res=[]
            while(len(que)!=0):
                ch=que.pop(0)
                res.append(ch)
                res.append(ch+[i])
            que = res
        return res 