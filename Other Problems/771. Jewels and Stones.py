from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(value for key, value in Counter(stones).items() if key in jewels)
