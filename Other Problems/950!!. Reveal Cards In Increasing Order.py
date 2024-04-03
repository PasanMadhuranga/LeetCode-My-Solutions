class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        ans = []
        for x in sorted(deck)[::-1]:
            ans = [x] + ans[-1:] + ans[:-1]
        return ans