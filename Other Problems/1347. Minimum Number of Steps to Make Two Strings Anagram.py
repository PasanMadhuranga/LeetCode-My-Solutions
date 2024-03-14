class Solution:
    def minSteps(self, s: str, t: str) -> int:
        firstStrOccurs = {}
        secondStrOccurs = {}
 
        for ch in s:
            if ch in firstStrOccurs:
                firstStrOccurs[ch] += 1
            else:
                firstStrOccurs[ch] = 1

        for ch in t:
            if ch in secondStrOccurs:
                secondStrOccurs[ch] += 1
            else:
                secondStrOccurs[ch] = 1

        answer = 0

        for key in firstStrOccurs:
            diff = firstStrOccurs[key] - secondStrOccurs.get(key, 0)
            if (diff > 0):
                answer += diff
        
        return answer


# Counter for String s: The function uses the Counter class from Python's collections module 
# to create a frequency count of all characters in string s. 
# This counter (cnt) is a dictionary where each key is a character from s and 
# its value is the number of times that character appears in s.
    
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt, steps = Counter(s), 0
        for c in t:
            if cnt[c] > 0:
                cnt[c] -= 1
            else:
                steps += 1
        return steps