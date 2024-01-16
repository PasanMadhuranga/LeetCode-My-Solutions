class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        finalWord = ""

        if (len1 <= len2): 
            maxWord = word2
            minLen = len1
        else: 
            maxWord = word1
            minLen = len2

        for i in range(minLen):
            finalWord += word1[i] + word2[i]

        return finalWord + maxWord[minLen:]
        

# Another Solution found in the discussion section
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)