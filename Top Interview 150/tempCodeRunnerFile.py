# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         index = 0
#         for i in range(len(nums)):
#             if (nums[index] != nums[i]):
#                 nums[index+1] = nums[i]
#                 index += 1

#         return index + 1