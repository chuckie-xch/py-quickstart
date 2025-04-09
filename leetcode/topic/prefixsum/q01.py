from itertools import accumulate
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s, mx, mn = 0, 0, 0
        for i, x in enumerate(nums):
            s += x
            mx = max(mx, s)
            mn = min(mn, s)
        return mx - mn

    def solution2(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)
