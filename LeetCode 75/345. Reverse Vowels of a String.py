class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        listS = list(s)
        length = len(s)
        left, right = 0, length - 1

        while (left <  right):
            if (listS[left] in vowels):
                if (listS[right] in vowels):
                    listS[left], listS[right] = listS[right], listS[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return ''.join(listS)


# Another Better Solution Found in the Discussion Section:
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        listS = list(s)
        length = len(s)
        left, right = 0, length - 1

        while (left < right):
            # Move the left pointer to the right until it finds a vowel
            while (left < right and listS[left] not in vowels):
                left += 1
            # Move the right pointer to the left until it finds a vowel
            while (left < right and listS[right] not in vowels):
                right -= 1
            # swap the vowels
            listS[left], listS[right] = listS[right], listS[left]
            # Move the pointers
            left += 1
            right -= 1

        return ''.join(listS)
        