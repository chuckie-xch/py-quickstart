from math import inf
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        pre_max, pre_min = -inf, inf
        for x in arrays:
            ans = max(ans, x[len(x) - 1] - pre_min, pre_max - x[0])
            pre_min = min(pre_min, x[0])
            pre_max = max(pre_max, x[len(x) - 1])

        return ans
