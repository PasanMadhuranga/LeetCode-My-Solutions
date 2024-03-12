class Solution:
    def minOperations(self, n: int) -> int:
        mid = n // 2
        if (n % 2 == 0): return mid ** 2
        return (mid + 1) * mid


# Another Solution found in the discussion section
class Solution:
    def minOperations(self, n: int) -> int:
        return n * n // 4
        