class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize an index to keep track of the position for unique elements
        index = 0

        # Iterate through the array
        for i in range(len(nums)):
            # Check if the current element is different from the element at the index
            if (nums[index] != nums[i]):
                # If it is different, increment the index and update the element at the new index
                nums[index + 1] = nums[i]
                index += 1

        # After processing, index + 1 will be the new length of the array without duplicates
        return index + 1



# Other solutions found in solutions
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		nums[:] = sorted(set(nums))
		return len(nums)
    # nums =  doesn't replace elements in the original list.
    # nums[:] = replaces element in place
     
     
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 1
        n = len(nums)
        for i in range(1, n):
            if (nums[i] != nums[i-1]):
                nums[result] = nums[i]
                result += 1

        return result