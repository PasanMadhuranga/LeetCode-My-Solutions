class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        for r in range(rows):
            diagArr = []
            diagR = r
            diagC = 0
            while (diagR < rows and diagC < cols):
                diagArr.append(mat[diagR][diagC])
                diagR += 1
                diagC += 1
            diagArr.sort()

            diagR = r
            diagC = 0
            while (diagR < rows and diagC < cols):
                mat[diagR][diagC] = diagArr[diagC]
                diagR += 1
                diagC += 1
        
        if (cols == 1): return mat
        for c in range(1, cols):
            diagArr = []
            diagC = c
            diagR = 0
            while (diagC < cols and diagR < rows):
                diagArr.append(mat[diagR][diagC])
                diagC += 1
                diagR += 1
            diagArr.sort()

            diagC = c
            diagR = 0
            while (diagC < cols and diagR < rows):
                mat[diagR][diagC] = diagArr[diagR]
                diagR += 1
                diagC += 1
        return mat
    
# Another Solution found in the discussion section
def diagonalSort(self, A):
    n, m = len(A), len(A[0])
    d = collections.defaultdict(list)
    for i in xrange(n):
        for j in xrange(m):
            d[i - j].append(A[i][j])
    for k in d:
        d[k].sort(reverse=1)
    for i in xrange(n):
        for j in xrange(m):
            A[i][j] = d[i - j].pop()
    return A