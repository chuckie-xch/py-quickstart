from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        m, n = len(a), len(b)
        if m == 1 and n == 1:
            return abs(a[0] - b[0])

        i, j, ans = 0, 0, float('inf')
        a.sort()
        b.sort()

        while i < m and j < n:
            if a[i] == b[j]:
                return 0
            ans = min(ans, abs(a[i] - b[j]))

            if a[i] < b[j]:
                i += 1
            else:
                j += 1

        return ans
