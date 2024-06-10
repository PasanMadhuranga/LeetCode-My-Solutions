from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return "" if str1 + str2 != str2 + str1 else str1[:gcd(len(str1), len(str2))]
        
# str1+str2 == str2+str1 if and only if str1 and str2 have a gcd .
# E.g. str1=abcabc, str2=abc, then str1+str2 = abcabcabc = str2+str1
# This(str1+str2==str2+str1) is a requirement for the strings to have a gcd. 
# If one of them is NOT a common part then gcd is "".It means we will return empty string
# Proof:-str1 = mGCD, str2 = nGCD, str1 + str2 = (m + n)GCD = str2 + str1
# Both the strings are made of same substring added multiple times.
# Since they are multiples, next step is simply to find the gcd of the lengths of 2 strings 
