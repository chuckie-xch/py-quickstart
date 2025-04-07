from functools import cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @cache
        def minChange(i: int, j: int) -> int:
            if i >= j:
                return 0
            return minChange(i + 1, j - 1) + (1 if s[i] != s[j] else 0)

        @cache
        def dfs(i: int, r: int) -> int:
            if i == 0:
                return minChange(0, r)

            return min(minChange(l, r) + dfs(i - 1, l - 1) for l in range(i, r + 1))

        return dfs(k - 1, len(s) - 1)
