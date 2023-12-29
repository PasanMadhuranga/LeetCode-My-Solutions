class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize a dictionary to keep track of the counts of each element.
        counts = {}

        # Calculate the majority count, which is more than half of the array's length.
        majority = len(nums) // 2

        # Iterate through each number in the array.
        for num in nums:
            # Check if the number is not already in the counts dictionary.
            if num not in counts:
                # Count how many times the current number appears in the array.
                numCount = nums.count(num)

                # If the count of the current number is greater than the majority count,
                # it is the majority element and can be returned immediately.
                if numCount > majority:
                    return num
                
                # Store the count of the current number in the counts dictionary.
                # This is to avoid recounting the same number in future iterations.
                counts[num] = numCount


# Another solution found in the discussion section.

# Moore Voting Algorithm
# The intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an array, it will always remain in the lead, even after encountering other elements.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate