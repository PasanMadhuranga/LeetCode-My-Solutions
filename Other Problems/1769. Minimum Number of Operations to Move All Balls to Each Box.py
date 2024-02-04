class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        answer = [0] * l
        for i in range(l):
            moves = 0
            for j in range(l):
                if (boxes[j] == "1"):
                    moves += abs(j-i)
            answer[i] = moves
        return answer


# Another solution found in the discussion section
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        answer = [0] * l
        leftCount, leftCost, rightCount, rightCost = 0, 0, 0, 0
        for i in range(1, l):
            if boxes[i-1] == '1': 
                leftCount += 1
            leftCost += leftCount 
            answer[i] = leftCost
        for i in range(l-2, -1, -1):
            if boxes[i+1] == '1': 
                rightCount += 1
            rightCost += rightCount
            answer[i] += rightCost
        return answer