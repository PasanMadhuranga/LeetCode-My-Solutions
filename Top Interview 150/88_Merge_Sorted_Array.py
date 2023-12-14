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


# Another Answer Found in Solutions
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Iterate as long as there are elements in nums2 to be merged.
        while (n > 0):
            # Check if there are elements in nums1 and the last element of the remaining nums1 is greater or equal
            # to the last element of nums2. This comparison is skipped if nums1 is empty (m == 0).
            if (m > 0 and nums1[m-1] >= nums2[n-1]):
                # Place the larger element (from nums1) at the end of the merged array.
                nums1[m+n-1] = nums1[m-1]
                m -= 1  # Move the pointer in nums1 to the left.
            else:
                # Place the larger element (from nums2) or if nums1 is empty, just copy from nums2.
                nums1[m+n-1] = nums2[n-1]
                n -= 1  # Move the pointer in nums2 to the left.