class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n, m, goodPairs = len(nums1), len(nums2), 0
        for i in range(n):
            for j in range(m):
                if (not (nums1[i] % (nums2[j] * k))):
                    goodPairs += 1

        return goodPairs

# Time complexity: O(n*m)
# Space complexity: O(1)

# Another solution using product() function
# product() This tool computes the cartesian product of input iterables. It is equivalent to nested for-loops.
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum(a % (b*k) == 0 for a, b in product(nums1, nums2))
