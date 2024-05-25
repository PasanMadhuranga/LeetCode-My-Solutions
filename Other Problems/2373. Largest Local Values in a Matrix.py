class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid)
        for r in range(size-2):
            for c in range(size-2):
                grid[r][c] = max(max(row[c:c+3]) for row in grid[r:r+3])
        
        return [row[:size-2] for row in grid[:size-2]]
