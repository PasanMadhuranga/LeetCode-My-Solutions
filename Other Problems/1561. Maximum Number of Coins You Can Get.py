class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l = len(piles)
        numOfPiles = l // 3
        maxCoins = 0
        for i in range(numOfPiles, l, 2):
            maxCoins += piles[i]
        
        return maxCoins
    

# Another solution found in the discussion section
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles) // 3::2])
