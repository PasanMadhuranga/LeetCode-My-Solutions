class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowCount = len(grid)
        colCount = len(grid[0])
        # as grid only contains zeros and ones, we can also calculate zeros in a row by (grid.length - row_ones)
        rowSums = [ ( 2 * row.count(1) - rowCount) for row in grid ]  
        # This counts the difference along the columns    
        colSums = [ (2 * col.count(1) - colCount) for col in zip(*grid) ] 

        diff = []
        for r in range(rowCount):
            newRow = []
            for c in range(colCount):
                newRow.append(rowSums[r] + colSums[c])
            diff.append(newRow)
        
        return diff


# Anohther solution found in the discussion section
class Solution(object):
    def onesMinusZeros(self, grid):
        m, n = len(grid), len(grid[0])

        row_ones = [0] * m
        col_ones = [0] * n

        # Count ones in each row and column
        for i in range(m):
            for j in range(n):
                row_ones[i] += grid[i][j]
                col_ones[j] += grid[i][j]

        # Calculate the difference matrix
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2 * (row_ones[i] + col_ones[j]) - m - n

        return grid
        