class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Start from the end of the list and move backwards
        i = len(nums) - 1
        
        # Loop through the list backwards
        while (i >= 0):
            # Check if the current element is equal to the value to be removed
            if (nums[i] == val):
                # If it is, delete the element from the list
                del nums[i]
            # Move to the previous element in the list
            i -= 1
        
        # After removing all instances of the value, return the new length of the list
        return len(nums)
