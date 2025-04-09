from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s, mn, ans = 0, 0, -inf
        for v in nums:
            s += v
            ans = max(ans, s - mn)
            mn = min(mn, s)
        return ans
