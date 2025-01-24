from functools import cache
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        @cache
        def dfs(i: int, j: int):
            if i < 0:
                return 0
            res = dfs(i - 1, j)
            total_value = 0
            for w in range(min(j, len(piles[i]))):
                total_value += piles[i][w]
                res = max(res, dfs(i - 1, j - w - 1) + total_value)
            return res

        return dfs(n - 1, k)
