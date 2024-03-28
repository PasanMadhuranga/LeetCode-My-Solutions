class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = [i for i in range(1, n+1)]
        curLen = len(nums)
        i = 0
        while (curLen != 1):
            i = (i + k - 1) % curLen
            del nums[i]
            curLen -= 1
        
        return nums[0]

# Other solutions found in the discussion section
class Solution {
public:
    int findTheWinner(int n, int k) {
        return recfindWinner(n, k) + 1;
    }

    int recfindWinner(int n, int k){
        if (n == 1) return 0;

        return (recfindWinner(n - 1, k) + k) % n;
    }
};


class Solution {
public:
    int helper(int n,int k){
        int ans = 0;
        for(int i=1; i<=n; i++){
            ans = (ans + k) % i;
        }
        return ans;
    }
    int findTheWinner(int n, int k) {
        return helper(n,k)+1;   //+1 is for conterting 0-based indexing to 1-based indexing
    }
};