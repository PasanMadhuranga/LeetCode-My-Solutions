class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        citationCounts = [0] * (l + 1)
        for c in citations:
            if (c >= l):
                citationCounts[l] += 1
            else:
                citationCounts[c] += 1
        
        higherPapersCount = 0
        for i in range(l, -1, -1):
            higherPapersCount += citationCounts[i]
            if (higherPapersCount >= i):
                return i

        return 0

# Explanation:
# The idea behind it is some bucket sort mechanisms. First, you may ask why bucket sort. 
# Well, the h-index is defined as the number of papers with reference greater than the number.
# So assume n is the total number of papers, if we have n+1 buckets, number from 0 to n, 
# then for any paper with reference corresponding to the index of the bucket, we increment the count for that bucket. 
# The only exception is that for any paper with larger number of reference than n, we put in the n-th bucket.
# Then we iterate from the back to the front of the buckets, whenever the total count exceeds the index of the bucket, 
# meaning that we have the index number of papers that have reference greater than or equal to the index. 
# Which will be our h-index result. The reason to scan from the end of the array is that 
# we are looking for the greatest h-index.
    


# Another solution found in the discussion section:
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))

# Explanation:
# citations = sorted(citations,reverse=True)
# result = []
# for index,value in enumerate(c):
# if index < value:
#   result.append(1)
# return sum(result)