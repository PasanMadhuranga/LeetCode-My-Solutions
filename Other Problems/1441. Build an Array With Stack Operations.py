class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        answer = []
        i = 1
        for ele in target:
            while (i != ele):
                answer.append("Push")
                answer.append("Pop")
                i += 1
            i += 1
            answer.append("Push")

        return answer
        

# Another solution found in the discussion section
class Solution:
    def buildArray(self, target, n):
        operations = []
        targetIndex = 0  # Pointer for target array
        currentNumber = 1  # Pointer for numbers 1 to n

        while targetIndex < len(target):
            if target[targetIndex] == currentNumber:
                # If the current number in the target array matches the current number 1 to n
                # Append "Push" operation and move both pointers
                operations.append("Push")
                targetIndex += 1
            else:
                # If the numbers don't match, append "Push" followed by "Pop" operation
                # and only move the current number pointer
                operations.append("Push")
                operations.append("Pop")
            currentNumber += 1

        return operations