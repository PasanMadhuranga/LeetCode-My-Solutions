class Solution:
    def maxScore(self, A: List[int], x: int) -> int:
        dp = [-x, -x]
        dp[A[0] & 1] = A[0]
        for i in range(1, len(A)):
            dp[A[i] & 1] = max(dp[A[i] & 1], dp[A[i] & 1 ^ 1] - x) + A[i]
        return max(dp)
    
# dp[A[0] & 1] = A[0] sets the starting score based on the parity of the first element in the array A. 
# The expression A[0] & 1 yields 0 if A[0] is even and 1 if A[0] is odd, 
# effectively choosing the index for the dp array. 
# This step initializes the DP table with the first element's value at the correct parity index.
    
# The current score for the same parity (dp[A[i] & 1]), indicating a continuation within the same parity group without a penalty.
# The score from switching parities (dp[A[i] & 1 ^ 1] - x), which takes the score from the opposite parity, 
# subtracts the penalty x, and then adds the current number's value A[i]. 
# The bitwise XOR ^ 1 toggles between 0 (even) and 1 (odd), 
# effectively accessing the opposite parity's score.