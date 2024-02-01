class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laserBeams = 0
        numOfRows = len(bank)
        preDevices = bank[0].count("1")
        curRow = 1
        while (curRow < numOfRows):
            curDevices = bank[curRow].count("1")
            if (curDevices):
                laserBeams += preDevices * curDevices
                preDevices = curDevices
            curRow += 1
        return laserBeams
            
        
# Another solution found in the discussion section
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        laserBeams = 0
        preDevices = 0
        for row in bank:
            curDevices = row.count("1")
            if (curDevices):
                laserBeams += preDevices * curDevices
                preDevices = curDevices
        return laserBeams
            
        
        