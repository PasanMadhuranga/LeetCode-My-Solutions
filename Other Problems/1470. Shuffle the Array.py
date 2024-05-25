class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m = 2*n
        yi = n
        xi = 1
        for i in range(1, m-1, 2):
            nums[i] = nums[i] + nums[yi] * 10000
            nums[i+1] = nums[i+1] + (nums[xi]%10000) * 10000
            yi += 1
            xi += 1

        for i in range(1, m-1):
            nums[i] = nums[i] // 10000
        return nums
        