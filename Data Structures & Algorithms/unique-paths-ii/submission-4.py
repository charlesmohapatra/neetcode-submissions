class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] == 1:
            return 0
        cache = [[0] * cols for _ in range(rows)]
        def count(grid, r, c, cache):
            if r == rows or c == cols:
                return 0
            if r == rows-1 and c == cols-1:
                return 1
            if grid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            cache[r][c] = count(grid, r+1, c, cache) + count(grid, r, c+1, cache)
            return cache[r][c]
        return count(obstacleGrid, 0, 0, cache)
        