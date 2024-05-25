class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        i = 0
        for word in words:
            if x in word:
                ans.append(i)
            i += 1
        return ans
        