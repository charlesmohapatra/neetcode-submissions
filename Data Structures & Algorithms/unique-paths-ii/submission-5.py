class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[rows-1][cols-1] == 1:
            return 0
        prevRow = [0] * cols
        cache = [[0] * cols for _ in range(rows)]
        cache[rows-1][cols-1] = 1
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    cache[i][j] = 0
                else:
                    if j == cols-1:
                        cache[i][j] += prevRow[j]
                    else:
                        cache[i][j] += cache[i][j+1] + prevRow[j]
            prevRow = cache[i]
        return cache[0][0]
            
        