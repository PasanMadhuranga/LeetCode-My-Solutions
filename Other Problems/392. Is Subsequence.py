class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        n = len(s)

        if (n == 0):
            return True

        for letter in t:
            if(letter == s[i]): 
                i += 1
                if (i >= n):
                    return True
        return False
        
# Another solution found in the discussion section
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)
