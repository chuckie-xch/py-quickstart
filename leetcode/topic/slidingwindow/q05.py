from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for in_, out in zip(nums[k - 1:], nums):
            counter[in_] += 1
            s += in_
            if len(counter) == k:
                ans = max(ans, s)
            s -= out
            counter[out] -= 1
            if counter[out] == 0:
                del counter[out]
        return ans
