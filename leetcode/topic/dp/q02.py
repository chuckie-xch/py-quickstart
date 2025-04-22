from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f0, f1, n = 0, 0, len(cost)
        for i in range(2, n + 1):
            new_f = min(f1 + cost[i - 1], f0 + cost[i - 2])
            f0 = f1
            f1 = new_f
        return f1
