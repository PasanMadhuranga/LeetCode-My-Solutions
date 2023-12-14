class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Iterate as long as there are elements in both arrays.
        while (m > 0 and n > 0):
            # Compare the last elements of the remaining parts of nums1 and nums2.
            if (nums1[m-1] >= nums2[n-1]):
                # If the last element of nums1 is larger or equal, place it in the correct position at the end.
                nums1[m+n-1] = nums1[m-1]
                m -= 1  # Move the pointer in nums1 to the left.
            else:
                # If the last element of nums2 is larger, place it in the correct position at the end.
                nums1[m+n-1] = nums2[n-1]
                n -= 1  # Move the pointer in nums2 to the left.

        # If there are any remaining elements in nums2, place them in nums1.
        # This is needed if nums2 had smaller elements left after nums1 is exhausted.
        while (n > 0):
            nums1[n-1] = nums2[n-1]
            n -= 1