class Solution:
    def sortVowels(self, s: str) -> str:
        allVowels = "AaEeIiOoUu"
        vowelIndices = []
        sVowels = []
        strArr = list(s)
        strLen = len(strArr)

        for i in range(0, strLen):
            if strArr[i] in allVowels:
                sVowels.append(strArr[i])
                vowelIndices.append(i)
        
        sVowels.sort()
        sVowelsLen = len(sVowels)

        for i in range(0, sVowelsLen):
            strArr[vowelIndices[i]] = sVowels[i]
        
        return ''.join(strArr)
        


# Another solution found in the discussion section
from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        # List of vowels in both uppercase and lowercase
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        
        # Count the occurrences of each character in the string
        count_char = Counter(s)
        
        # Initialize an empty list to hold the vowels found in the string
        s_vowels = []
        
        # Iterate over the characters in the string (using keys from the counter to avoid duplicates)
        for char in count_char.keys():
            # If the character is a vowel, add it to the list of vowels
            # and replace all its occurrences in the string with '_'
            if char in vowels:
                s_vowels.append(char)
                s = s.replace(char, '_')
        
        # Sort the list of vowels in nondecreasing order of their ASCII values
        s_vowels.sort()
        
        # Replace the placeholders ('_') in the string with the sorted vowels
        # respecting their counts in the original string
        for char in s_vowels:
            s = s.replace('_', char, count_char[char])
        
        # Return the modified string with vowels sorted and consonants in their original positions
        return s
