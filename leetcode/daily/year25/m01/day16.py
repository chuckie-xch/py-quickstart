from cmath import inf
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = inf
        for i in range(n):
            val = nums[i]
            for j in range(i, n):
                val = val | nums[j]
                if val >= k:
                    res = min(res, j - i + 1)
                    break
        return res if res != inf else -1

