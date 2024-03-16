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
    



long long maxScore(vector<int>& n, int x) {
    long long eve = n[0] - (n[0] % 2 ? x : 0);
    long long odd = n[0] - (n[0] % 2 ? 0 : x);
    for (int i = 1; i < n.size(); ++i)
        if (n[i] % 2)
            odd = n[i] + max(odd, eve - x);
        else
            eve = n[i] + max(eve, odd - x);
    return max(eve, odd);
}

# The solution code implements a strategy to maximize the total score you can get, 
# taking into account the movement rules and how moving between positions with different parities (odd or even numbers) affects your score. Here's a simplified explanation of how it works:

# Initialization:
# eve: This represents the maximum score you can achieve when you are at an even number in the array. 
# It's initially set to n[0] minus x if n[0] is even (because you haven't moved yet, 
# but the condition applies as if you moved from an odd number to start here).
# odd: This is the maximum score you can achieve when you are at an odd number in the array, 
# initialized in a similar way to eve but considering the opposite parity condition.

# Iterating through the array:
# The loop starts from the second element (index 1) and checks each number's parity.
# If the current number (n[i]) is odd, it updates the odd score. 
# The new odd score is the current number plus the greater of:
# The previous odd score (staying on an odd number).
# The eve score minus x (moving from an even to an odd number, which incurs a penalty).
# If the current number is even, it similarly updates the eve score based on whether 
# it's more advantageous to stay even or move from odd to even, considering the penalty.

# Maximizing Score:
# After evaluating all elements in the array, the function returns the maximum of the eve and odd scores. 
# This represents the highest score achievable following the rules, 
# considering all possible moves and the penalties for moving between numbers of different parities.
# In essence, this solution dynamically keeps track of the best scores achievable 
# for each parity at each step, considering the penalty for moving between different parities. 
# The goal is to find the optimal path through the array that maximizes the total score, 
# accounting for the potential penalty when necessary.