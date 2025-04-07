from collections import Counter
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = Counter(a + b for a in nums1 for b in nums2)
        return sum(cnt[-x - y] for x in nums3 for y in nums4)
