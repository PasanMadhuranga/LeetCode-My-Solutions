class Solution:
    def convertToBase(self, num: int, base: int) -> str:
        result = ""
        while (num >= base):
            result = str(num % base) + result
            num //= base 

        return str(num) + result


    def isPalindrome(self, num: str) -> bool:
        l = len(num)
        limit = l // 2

        for i in range(limit):
            if (num[i] != num[l - 1- i]):
                return False
        return True


    def isStrictlyPalindromic(self, n: int) -> bool:
        for b in range(2, n - 1):
            if(not self.isPalindrome(self.convertToBase(n, b))):
                return False
        
        return True

# Another Solution found in the discussion section
# The condition is extreme hard to satisfy, think about it...
# for every base b between 2 and n - 2...
# 4 is not strictly palindromic number
# 5 is not strictly palindromic number
# ..
# then the bigger, the more impossible.
# Just return false