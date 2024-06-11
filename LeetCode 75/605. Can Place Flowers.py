class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bedSize = len(flowerbed)
        i = 0
        while (i < bedSize):
            if (flowerbed[i]):
                i += 2
            else:
                try:
                    if (flowerbed[i+1]):
                        i += 3
                    else:
                        n -= 1
                        i += 2
                except:
                    n -= 1
                    i += 2
            if (n <= 0):
                return True
        return False
    

# Another Solution Found in the Discussion Section:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False