class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}
        n = len(s)
        for i in range(n):
            alphabet_dict[s[i]] += i
            alphabet_dict[t[i]] -= i
        
        return sum(abs(value) for value in alphabet_dict.values())