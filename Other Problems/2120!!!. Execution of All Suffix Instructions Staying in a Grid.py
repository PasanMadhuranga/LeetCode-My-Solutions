class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        l = len(s)
        answer = []
        
        for i in range(l):
            moveCount = 0
            curPos = startPos.copy()
            for j in range(i, l):
                if (s[j] == "U"):
                    curPos[0] -= 1
                elif (s[j] == "D"):
                    curPos[0] += 1
                elif (s[j] == "L"):
                    curPos[1] -= 1
                else:
                    curPos[1] += 1
                
                if (not ((0 <= curPos[0] < n) and (0 <= curPos[1] < n))):
                    break
                moveCount += 1
            answer.append(moveCount)
        return answer


# Another colution found in the discussion section
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        m = len(s)
        direc = {'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}
        upmost = startPos[0] + 1
        downmost = n - startPos[0]
        leftmost = startPos[1] + 1
        rightmost = n - startPos[1]
        curr_row,curr_col = 0,0    
        next_row,next_col = {0:m}, {0:m}
        ans = []
        
        for i in range(m-1,-1,-1):
            curr_row -= direc[s[i]][0]
            curr_col -= direc[s[i]][1]
            maxstep = m-i
            if curr_row - upmost in next_row:  
                maxstep = min(maxstep,  next_row[curr_row - upmost] - i - 1 )
            if curr_row + downmost in next_row:  
                maxstep = min(maxstep,  next_row[curr_row + downmost] - i - 1 )
            if curr_col - leftmost in next_col:  
                maxstep = min(maxstep,  next_col[curr_col - leftmost] - i - 1 )
            if curr_col + rightmost in next_col: 
                maxstep = min(maxstep,  next_col[curr_col + rightmost] - i - 1 )
            next_row[curr_row] = i
            next_col[curr_col] = i
            ans.append(maxstep)
            
        return ans[::-1]