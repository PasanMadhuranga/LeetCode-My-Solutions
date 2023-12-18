class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0  # Initialize a variable to keep track of the position for the next unique element
        duplicates = 1  # Initialize a counter to track the number of duplicates encountered
        n = len(nums)  # Length of the input array
        i = 1  # Start iterating from the second element

        # Iterate over the array starting from the second element
        while (i < n):
            # Check if the current element is different from the previous one
            if (nums[i-1] != nums[i]):
                result += 1  # Increment result to move to the next unique position
                # Check if there were 2 or more duplicates of the previous number
                if (duplicates >= 2):
                    nums[result] = nums[i-1]  # Copy the duplicate value
                    result += 1  # Increment result to skip the duplicate
                    nums[result] = nums[i]  # Copy the current unique value
                    duplicates = 1  # Reset the duplicates counter
                elif (duplicates == 1):  # If only one instance of previous number was found
                    nums[result] = nums[i]  # Copy the current number
            else:
                duplicates += 1  # Increment duplicates counter for consecutive duplicates
            i += 1  # Move to the next element

        # Check for any remaining duplicates of the last number
        if (duplicates >= 2):
            result += 1  # Increment result to accommodate the duplicate
            nums[result] = nums[i-1]  # Copy the last duplicate
        
        return result + 1  # Return the length of the array with at most two duplicates of each number



# Another solution found in solutions
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

