class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(1, n):
            for j in range(n-i):
                nums[j] = (nums[j] + nums[j + 1]) % 10
        return nums[0]


# Another solution found in the discussion section
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = 0
        m = len(nums) - 1
        mck, exp2, exp5 = 1, 0, 0
        inv = (0, 1, 0, 7, 0, 0, 0, 3, 0, 9)
        for k, num in enumerate(nums):
            if not (exp2 and exp5):
                mCk_ = mck * (6, 2, 4, 8)[exp2 % 4] if exp2 else 5 * mck if exp5 else mck
                result = (result + mCk_ * num) % 10
            if k == m:
                return result

            # mCk *= m - k
            mul = m - k
            while not mul % 2:
                mul //= 2
                exp2 += 1
            while not mul % 5:
                mul //= 5
                exp5 += 1
            mck = mck * mul % 10

            # mCk //= k + 1
            div = k + 1
            while not div % 2:
                div //= 2
                exp2 -= 1
            while not div % 5:
                div //= 5
                exp5 -= 1
            mck = mck * inv[div % 10] % 10
            
            