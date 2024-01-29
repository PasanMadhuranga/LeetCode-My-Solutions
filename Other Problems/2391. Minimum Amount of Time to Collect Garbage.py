class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        metalNotFound, paperNotFound, glassNotFound = True, True, True
        totmins = 0
        i = len(garbage) - 1
        while (i > 0 and (metalNotFound or paperNotFound or glassNotFound)):
            if (metalNotFound and "M" in garbage[i]):
                totmins += sum(travel[:i])
                metalNotFound = False
            if (paperNotFound and "P" in garbage[i]):
                totmins += sum(travel[:i])
                paperNotFound = False
            if (glassNotFound and "G" in garbage[i]):
                totmins += sum(travel[:i])
                glassNotFound = False
            i -= 1
        
        return totmins + sum(len(s) for s in garbage)


# Another Solution found in the discussion section
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n=len(garbage)
        tG, tP, tM=0, 0, 0
        Time=0
        for i in range(n-1, -1, -1):
            x=garbage[i]
            Time+=len(x)
            if tG==0 and x.find('G')!=-1: tG=i 
            if tP==0 and x.find('P')!=-1: tP=i
            if tM==0 and x.find('M')!=-1: tM=i
        Time+=sum(travel[:tG])+sum(travel[:tP])+sum(travel[:tM])
        return Time