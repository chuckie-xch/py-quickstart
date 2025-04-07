from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = mx = 0
        for i, v in enumerate(values):
            ans = max(ans, v - i + mx)
            mx = max(mx, v + i)
        return ans