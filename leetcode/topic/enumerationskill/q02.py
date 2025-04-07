from math import inf
from typing import List


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = inf
        mapping = {}
        for i, v in enumerate(cards):
            if v in mapping:
                ans = min(ans, i - mapping[v] + 1)
            mapping[v] = i
        return ans if ans < inf else -1
