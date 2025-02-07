from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirs = (0, 1), (1, 0), (0, -1), (-1, 0)
        ans = [[0] * n for _ in range(n)]
        i = j = di = 0
        for val in range(1, n * n + 1):
            ans[i][j] = val
            x = i + dirs[di][0]
            y = j + dirs[di][1]
            if x < 0 or x >= n or y < 0 or y >= n or ans[x][y] != 0:
                di = (di + 1) % 4

            i += dirs[di][0]
            j += dirs[di][1]
        return ans
