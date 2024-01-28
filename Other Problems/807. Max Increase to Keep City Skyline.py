class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        sumHeight = 0
        for i in range (cols):
            currCol = [row[i] for row in grid]
            colMin = max(currCol)
            for j in range (rows):
                incHeight = min(max(grid[j]), colMin) - grid[j][i]
                if (incHeight > 0):
                    sumHeight += incHeight
        return sumHeight


# Another Solution found in the discussion section
# class Solution {
#     public int maxIncreaseKeepingSkyline(int[][] grid) {
#         int n = grid.length;
#         int[] col = new int[n], row = new int[n];
#         for (int i = 0; i < n; i++) {
#             for (int j = 0; j < n; j++) {
#                 row[i] = Math.max(row[i], grid[i][j]);
#                 col[j] = Math.max(col[j], grid[i][j]);
#             }
#         }
#         int res = 0;
#         for (int i = 0; i < n; i++)
#             for (int j = 0; j < n; j++)
#                 res += Math.min(row[i], col[j]) - grid[i][j];
#         return res;
#     }
}