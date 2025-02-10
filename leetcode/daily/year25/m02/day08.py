from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = dfs(i - 1, j) + dfs(i, j - 1)
            return memo[i][j]

        return dfs(m - 1, n - 1)
